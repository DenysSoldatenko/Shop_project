from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['content'] = "Welcome to Luxe Living!"
        return context


class AboutView(TemplateView):
    template_name = 'core/info_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['content'] = "About Us - Luxe Living Furniture"
        context['text_on_page'] = """
            At Luxe Living, we believe that your home is more than just a place — it's a sanctuary where unforgettable moments are created.

            Our mission is simple: L.U.X.E. — Living Unmatched eXperiences Everywhere. 

            Whether you're hosting friends, enjoying a family movie night, or simply relaxing with a book, we offer high-quality, stylish, and affordable furniture to make your space truly your own.

            Passionate about design and functionality, Luxe Living is your go-to destination for bringing comfort, sophistication, and innovation into your home. Browse our curated collections and see why our customers trust us to make their homes a reflection of their style and personality!
        """
        return context


class DeliveryAndPaymentView(TemplateView):
    template_name = 'core/info_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delivery and Payment'
        context['content'] = "Delivery and Payment Information"
        context['text_on_page'] = """
            Welcome to Luxe Living's Delivery and Payment Information! We are thrilled to provide you with a seamless and exciting shopping experience, ensuring your order gets to you quickly, safely, and with ease!

            Exciting Delivery Options:
            - Standard Delivery: Reliable and affordable. Your furniture will arrive in just a few days.
            - Express Delivery: Need it faster? Opt for express delivery and get your order delivered within 2-3 days!
            - Same-day Delivery: In select locations, we offer same-day delivery — perfect for last-minute purchases or urgent needs! Imagine receiving your dream furniture on the same day you place the order!

            Flexible Payment Methods:
            - Credit/Debit Cards: Pay with major credit or debit cards, securely processed with encryption technology.
            - PayPal: A fast and easy option to complete your purchase with just a few clicks.
            - Cash on Delivery: For your convenience, we offer cash on delivery in selected locations! Pay when your furniture arrives — no need to worry about upfront payments.

            We aim to make your shopping experience effortless, so you can focus on what matters most: creating a home that truly reflects your style and personality.

            Thank you for choosing Luxe Living, where quality meets comfort.
        """
        return context


class ContactInformationView(TemplateView):
    template_name = 'core/info_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us - We’re Here to Help!'
        context['content'] = "Contact Information"
        context['text_on_page'] = """
            We're so glad you reached out! At Luxe Living, we're always ready to assist you and answer any questions you have. Whether it's about our products, services, or anything else, our team is excited to help!

            Customer Support:
            - 📧 Email: support@luxeliving.com
            - 📞 Phone: +1 800 123 4567
            - 🕒 Hours: Monday to Friday, 9:00 AM - 5:00 PM (We can't wait to hear from you!)

            Visit Us:
            Come visit us in person and experience Luxe Living firsthand! We're located at:
            Luxe Living Store
            1234 Luxury St, Suite 100
            City, State, ZIP

            Stay Connected:
            - 📱 Facebook: @LuxeLivingFurniture
            - 📸 Instagram: @LuxeLiving
            We love connecting with our community, so follow us and stay up to date on all things Luxe Living!

            We're here for you — let's make your home dreams come true! 😍
        """
        return context
