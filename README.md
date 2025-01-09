## Opis projektu

Aplikacja Voting App to prosty system głosowania, w którym użytkownik może oddać głos na kota 🐱 lub psa 🐶. Wyniki głosowania są zapisywane w bazie danych Redis i prezentowane w osobnym interfejsie.

## Struktura projektu

• vote: Usługa frontendowa pozwalająca użytkownikowi oddać głos. Dostępna pod portem 5000.
    
• result: Usługa wyświetlająca wyniki głosowania. Dostępna pod portem 5001.
    
• redis: Baza danych Redis przechowująca liczbę głosów. Dostępna na porcie 6379.

## Wymagania

    Docker
    Docker Compose

## Jak uruchomić projekt?

Upewnij się, że masz zainstalowany Docker i Docker Compose.

W katalogu projektu uruchom poniższe polecenie:
```bash
docker compose up
```

Aplikacja uruchomi trzy usługi:

• Głosowanie (Vote): http://localhost:5000

• Wyniki (Result): http://localhost:5001

• Redis: http://localhost:6379

Aby zakończyć działanie aplikacji, użyj kombinacji klawiszy Ctrl+C, a następnie:

    docker-compose down

## Uwagi

W przypadku problemów upewnij się, że porty 5000, 5001 i 6379 nie są zajęte przez inne procesy.
Wszystkie dane przechowywane są w pamięci Redis. Po zakończeniu działania kontenerów dane zostaną utracone.

Miłego korzystania z aplikacji! 🎉

