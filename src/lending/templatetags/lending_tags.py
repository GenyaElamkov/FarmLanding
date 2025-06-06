from django import template

from ..models import (
    Hero,
    AboutFarm,
    About,
    Product,
    Gallery,
    Review,
    Contacts,
    SocialNetwork,
)


register = template.Library()


@register.inclusion_tag("lending/hero.html")
def show_hero():
    title = Hero.objects.first()
    if title:
        return {
            "title": title.title,
            "description": title.description,
            "image": title.image,
        }
    return {}


@register.inclusion_tag("lending/about_farm.html")
def show_about_farm():
    data = AboutFarm.objects.all()
    return {"about_farm": data}


@register.inclusion_tag("lending/products.html")
def show_all_products():
    """Отоброжает продукты"""
    products = Product.objects.all()
    return {"products": products}


@register.inclusion_tag("lending/gallery.html")
def show_all_gallery():
    """Отоброжает images в галерее"""
    images = Gallery.objects.all()
    return {"images": images}


@register.inclusion_tag("lending/about.html")
def show_about():
    """Отоброжает блок о нас"""
    data = About.objects.first()
    if data:
        return {
            "title": data.title,
            "description": data.description,
            "image": data.image,
        }
    return {}


@register.inclusion_tag("lending/reviews.html")
def show_reviews():
    reviews = Review.objects.all()
    return {"reviews": reviews}


@register.inclusion_tag("lending/contacts.html")
def show_contacts():
    contacts = Contacts.objects.first()
    if contacts:
        return {
            "address": contacts.address,
            "phone": contacts.phone.as_national,
            "email": contacts.email,
        }
    return {}

@register.inclusion_tag("lending/social_network.html")
def show_social_network():
    socials = SocialNetwork.objects.all()
    return {'socials': socials}
