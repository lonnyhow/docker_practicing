from ninja import Router
from apps.blog_api.schemas.faqs import FaqCreateSchema, FaqsSchema
from apps.main.models import FAQ
from django.shortcuts import get_object_or_404

faqs_router = Router(tags=['FAQs'])

@faqs_router.get('/api/faqs/', response=list[FaqsSchema])
def get_faqs(request):
    faqs = FAQ.objects.all()
    return faqs



@faqs_router.put('/api/faqs/{faq_id}/create/', response=FaqCreateSchema)
def create_faqs(request, data: FaqCreateSchema):
    is_question_exists = FAQ.objects.filter(question=data.question)
    if is_question_exists.exists():
        obj = is_question_exists.first()
        obj.answer = data.answer
        obj.save()
        return obj

    new_faq = FAQ.objects.create(**data.model_dump())
    return new_faq

@faqs_router.delete('/api/faqs/{faq_id}/')
def delete_category(request, faq_id: int):
    faq = get_object_or_404(FAQ, pk=faq_id)
    faq.delete()
    return {'success': True}



