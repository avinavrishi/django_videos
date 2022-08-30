from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 16

#Category page View
def CategoryView(request):
    allCategories={}
    allCategory =  Post.objects.values('Post_category','imagefile')
    evt = { item['Post_category'] for item in allCategory }
    cat_list = list(evt)
    evt2 = [ item['imagefile'] for item in allCategory ]
    

    for ev in cat_list:
        x = Post.objects.filter(Post_category=ev)
        allCategories[ev] = x

    params = {'Category_list': allCategories}

    return render(request,'CategoryPage.html', params)



#Category view page
def CategoryFileView(request, category):
    allcategory = Post.objects.filter(Post_category = category)

    paginator = Paginator(allcategory, 2) # Show 8 video per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    params = {'Category':allcategory , 'page_obj':page_obj}

    return render(request,'CategoryPageFile.html', params)


#category vidoes page
def SearchPageView(request, query):
    allcategory = Post.objects.filter(keywords__contains = query)

    paginator = Paginator(allcategory, 16) # Show 8 video per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    params = {'Category':allcategory , 'page_obj':page_obj}

    return render(request,'SearchPage.html', params)


#Post detail page Video player page
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    cat = post.Post_category
    category = Post.objects.filter(keywords__contains = cat)
    paginator = Paginator(category, 8) # Show 8 video per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    keywords = post.keywords
    keywords_list = keywords.split()


    #Handling comment query set
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'Category': category,
                                           'Keywords': keywords_list,
                                           'page_obj':page_obj })
