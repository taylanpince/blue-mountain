from django import template

from content_blocks.models import ContentBlock


register = template.Library()


@register.inclusion_tag("content_blocks/block.html")
def content_block(slug):
    """
    Renders the block with the given name
    """
    try:
        block = ContentBlock.objects.get(slug=slug)
    except ContentBlock.DoesNotExist:
        block = None

    return {
        "content_block": block,
    }
