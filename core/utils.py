from django.conf import settings
from django.core.mail import send_mail


def send_appilcation_mail(application, email):
    dd = send_mail(
        subject="APPLICATION TO A PRODUCT OF COMPANY FROM CAR SHOP",
        message=f"""from {application.full_name} with phone number {application.phone_number} to product 
        {application.product.name} with product code {application.product.product_code}\n
        WITH COMMENT {application.comment}""",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
