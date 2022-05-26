from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Asset


class AssetList(generic.ListView):
    model = Asset
    queryset = Asset.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 6

class AssetDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Asset.objects.filter(status=1)
        asset = get_object_or_404(queryset, slug=slug)
        comments = asset.comments.filter(approved=True).order_by('created_on')
        
        return render(
            request,
            "asset_detail.html",
            {
                "asset": asset,
                "comments": comments,
            },
        )
