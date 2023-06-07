from django.utils.text import slugify

def slugify_instances(instance, save=False, new_slug=None): #auto slug generate
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(f"{instance.fname}-{instance.lname}-{instance.birth_date}") #slug contains, First Name, Last Name and Birth Date
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        #if for some reason the universe conspires to exist two people who were born on the same day with the same first and last name
        #this function solves it by putting their number in the slug
        slug = slugify(f"{slug}-{Klass.objects.count() +1}")
    instance.slug = slug
    if save:
        return instance


from django.contrib.auth.decorators import user_passes_test

def superuser_required(view_func):
    #chek if it`s a super user
    return user_passes_test(
        lambda u: u.is_superuser,
        login_url='login',
        redirect_field_name=None,
    )(view_func)