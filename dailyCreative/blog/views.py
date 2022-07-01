from django.shortcuts import render


# Create your views here.
def about_us(request):
    return render(request, 'blog/about-us.html')


def blog_details(request):
    return render(request, 'blog/blog-details.html')


def blog_details_1(request):
    return render(request, 'blog/blog-details1.html')


def cart(request):
    return render(request, 'blog/cart.html')


def category(request):
    return render(request, 'blog/category.html')


def category_detail(request):
    return render(request, 'blog/category-detail.html')


def checkout(request):
    return render(request, 'blog/checkout.html')


def coming_soon(request):
    return render(request, 'blog/coming-soon.html')


def contact_us(request):
    return render(request, 'blog/contact-us.html')


def dashboard(request):
    return render(request, 'blog/dashboard.html')


def dashboard_addtour(request):
    return render(request, 'blog/dashboard-addtour.html')


def dashboard_booking(request):
    return render(request, 'blog/dashboard-booking.html')


def dashboard_history(request):
    return render(request, 'blog/dashboard-history.html')


def dashboard_list(request):
    return render(request, 'blog/dashboard-list.html')


def dashboard_my_profile(request):
    return render(request, 'blog/dashboard-my-profile.html')


def dashboard_reviews(request):
    return render(request, 'blog/dashboard-reviews.html')


def error(request):
    return render(request, 'blog/error.html')


def faq(request):
    return render(request, 'blog/faq.html')


def forgot_password(request):
    return render(request, 'blog/forgot-password.html')


def index(request):
    return render(request, 'blog/index.html')


def index_1(request):
    return render(request, 'blog/index-1.html')


def index_2(request):
    return render(request, 'blog/index-2.html')


def index_3(request):
    return render(request, 'blog/index-3.html')


def index_4(request):
    return render(request, 'blog/index-4.html')


def index_5(request):
    return render(request, 'blog/index-5.html')


def index_6(request):
    return render(request, 'blog/index-6.html')


def login(request):
    return render(request, 'blog/login.html')


def mag(request):
    return render(request, 'blog/mag.html')


def mag_fashion(request):
    return render(request, 'blog/mag-fashion.html')


def mag_fitness(request):
    return render(request, 'blog/mag-fitness.html')


def mag_food(request):
    return render(request, 'blog/mag-food.html')


def mag_photo(request):
    return render(request, 'blog/mag-photo.html')


def mag_sports(request):
    return render(request, 'blog/mag-sports.html')


def mag_tech(request):
    return render(request, 'blog/mag-tech.html')


def mag_travel(request):
    return render(request, 'blog/mag-travel.html')


def post_details(request):
    return render(request, 'blog/post-details.html')


def shop(request):
    return render(request, 'blog/shop.html')


def shop_detail(request):
    return render(request, 'blog/shop-detail.html')


def tag(request):
    return render(request, 'blog/tag.html')


def tag_detail(request):
    return render(request, 'blog/tag-detail.html')


def tag_details(request):
    return render(request, 'blog/tag-details.html')
