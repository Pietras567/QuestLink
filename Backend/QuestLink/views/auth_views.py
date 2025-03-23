import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from sqlalchemy.orm import Session

from QuestLink.models.user_models import Account, User

def get_account_by_credentials(login_input, password_input):
    # Tu należy wykonać zapytanie do bazy danych (np. używając SQLAlchemy) oraz
    # zweryfikować hasło (pamiętaj o bezpiecznym porównaniu i haszowaniu haseł)
    # Poniższy kod to tylko przykład:
    #

    session = Session()
    account = session.query(Account).filter_by(login=login_input).first()
    if account and verify_password(password_input, account.password):
        return account
    # return None
    return None  # Placeholder – należy zastąpić implementacją


# Analogicznie, funkcja pobierająca użytkownika na podstawie konta
def get_user_by_account(account):
    # Przykładowa implementacja:
    #
    # from db_session import Session
    # from user_models import User
    # session = Session()
    # user = session.query(User).filter_by(id=account.user_id).first()
    # return user
    return None  # Placeholder – należy zastąpić implementacją


@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    try:
        data = json.loads(request.body.decode())
        login_input = data.get('login')
        password_input = data.get('password')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Błędny format danych.'}, status=400)

    if not login_input or not password_input:
        return JsonResponse({'error': 'Login oraz hasło są wymagane.'}, status=400)

    # Uzyskujemy konto użytkownika na podstawie podanych danych
    account = get_account_by_credentials(login_input, password_input)
    if account is None:
        return JsonResponse({'error': 'Niepoprawne dane logowania.'}, status=401)

    # Pobieramy obiekt użytkownika powiązany z kontem
    user = get_user_by_account(account)
    if user is None:
        return JsonResponse({'error': 'Nie znaleziono użytkownika.'}, status=404)

    # Jeżeli chcesz dodatkowo sprawdzić, czy użytkownik jest aktywny, możesz dodać warunek:
    # if not user.is_active:
    #     return JsonResponse({'error': 'Użytkownik nieaktywny.'}, status=403)

    # Generujemy token przy użyciu Django Simple JWT
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    })


def logout(request):
    pass

def register(request):
    pass

def token_refresh(request):
    pass

@require_http_methods(["GET"])
def echo(request):
    return HttpResponse("Hello World!")
