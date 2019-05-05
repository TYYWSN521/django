
# class PostFeed(Feed):
#
#     title = '标题'
#     description = '摘要'
#     link = '/'
#
#     def items(self, item):
#         return Post.objects.all()
#
#     def item_title(self, item):
#         return item.title
#
#     def item_description(self, item):
#         return item.summary
#
#     def item_link(self, item):
#         return reverse('blog:detail', args=(item.id,))
