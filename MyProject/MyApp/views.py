import random
import string
from django.shortcuts import render


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = list(string.ascii_lowercase)

    if use_uppercase:
        characters.extend(string.ascii_uppercase)
    if use_numbers:
        characters.extend(string.digits)
    if use_symbols:
        characters.extend(string.punctuation)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def password_generator_view(request):
    generated_password = ''

    if request.method == 'POST':
        length_str = request.POST.get('length', '8')  # Default to '8' if missing
        length = int(length_str) if length_str.isdigit() else 8  # Validate input
        
        use_uppercase = request.POST.get('use_uppercase') == 'on'
        use_numbers = request.POST.get('use_numbers') == 'on'
        use_symbols = request.POST.get('use_symbols') == 'on'

        generated_password = generate_password(length, use_uppercase, use_numbers, use_symbols)

    return render(request, 'MyAppHTML/password_generator.html', {'generated_password': generated_password})

