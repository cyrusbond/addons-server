from django.contrib import admin

from olympia.amo.admin import AMOModelAdmin

from .models import NeedsHumanReview, ReviewActionReason, UsageTier


class ReviewActionReasonAdmin(AMOModelAdmin):
    list_display = ('name', 'addon_type', 'is_active')
    list_filter = (
        'addon_type',
        'is_active',
    )
    fields = (
        'name',
        'is_active',
        'canned_response',
        'canned_block_reason',
        'addon_type',
        'cinder_policy',
    )
    raw_id_fields = ('cinder_policy',)
    view_on_site = False


admin.site.register(ReviewActionReason, ReviewActionReasonAdmin)


class UsageTierAdmin(AMOModelAdmin):
    list_display = (
        'slug',
        'name',
        'lower_adu_threshold',
        'upper_adu_threshold',
    )
    view_on_site = False
    fields = (
        'slug',
        'name',
        'lower_adu_threshold',
        'upper_adu_threshold',
        'growth_threshold_before_flagging',
        'abuse_reports_ratio_threshold_before_flagging',
    )


admin.site.register(UsageTier, UsageTierAdmin)


class NeedsHumanReviewAdmin(AMOModelAdmin):
    list_display = ('addon_guid', 'version', 'created', 'reason', 'is_active')
    list_filter = ('is_active',)
    raw_id_fields = ('version',)
    view_on_site = False
    list_select_related = ('version', 'version__addon')
    fields = ('created', 'modified', 'reason', 'version', 'is_active')
    readonly_fields = ('reason', 'created', 'modified')
    list_filter = (
        'reason',
        'is_active',
        'created',
    )

    actions = ['deactivate_selected', 'activate_selected']

    def deactivate_selected(modeladmin, request, queryset):
        for obj in queryset:
            # This will also trigger <Version>.reset_due_date(), which will
            # clear the due date if it's no longer needed.
            obj.update(is_active=False)

    def activate_selected(modeladmin, request, queryset):
        for obj in queryset:
            # This will also trigger <Version>.reset_due_date(), which will
            # set the due date if there wasn't one.
            obj.update(is_active=True)

    def addon_guid(self, obj):
        return obj.version.addon.guid


admin.site.register(NeedsHumanReview, NeedsHumanReviewAdmin)
