import torch
from transformers import pipeline
from PIL import Image
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Complaint

# Hugging Face pipelines
sentiment_classifier = pipeline("sentiment-analysis")
image_classifier = pipeline("zero-shot-image-classification")

def submit_complaint(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        complaint_text = request.POST['complaint']
        
        # Sentiment analysis on the complaint text
        sentiment_result = sentiment_classifier(complaint_text)
        sentiment = sentiment_result[0]['label']

        # Image analysis if an image is provided
        image_classification = "No image provided"
        if 'complaintImage' in request.FILES:
            image = Image.open(request.FILES['complaintImage'])
            candidate_labels = ["cleanliness", "security", "emergency"]
            image_result = image_classifier(image, candidate_labels=candidate_labels)
            image_classification = image_result[0]['label']
        
        # Save complaint to database
        complaint = Complaint(
            name=name,
            email=email,
            complaint_text=complaint_text,
            sentiment=sentiment,
            image_classification=image_classification
        )
        complaint.save()

     
    return render(request, 'submit_complaint.html')
# complaints/views.py
from django.shortcuts import render
from .models import Complaint

def admin_dashboard(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard.html', {'complaints': complaints})