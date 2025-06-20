import re
import math

# Carica un dizionario di password comuni (usalo se esiste)
def load_common_passwords(filepath="common_passwords.txt"):
    try:
        with open(filepath, "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"\W", password):
        charset += 32  # simboli comuni
    entropy = len(password) * math.log2(charset) if charset else 0
    return round(entropy, 2)

def password_strength(password, common_passwords):
    score = 0
    feedback = []

    # Lunghezza
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("La password è troppo corta (minimo 8 caratteri).")

    # Caratteri
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Aggiungi lettere minuscole.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Aggiungi lettere maiuscole.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Aggiungi numeri.")
    if re.search(r"\W", password):
        score += 1
    else:
        feedback.append("Aggiungi simboli (es. !, @, #).")

    # Parole comuni
    if password.lower() in common_passwords:
        score = 0
        feedback = ["La password è troppo comune!"]
    
    # Entropia
    entropy = calculate_entropy(password)

    # Valutazione finale
    if score >= 6 and entropy > 50:
        strength = "Forte "
    elif score >= 4:
        strength = "Media "
    else:
        strength = "Debole "

    return strength, entropy, feedback

if __name__ == "__main__":
    password = input("Inserisci una password da analizzare: ")
    common_pwds = load_common_passwords()
    strength, entropy, tips = password_strength(password, common_pwds)

    print(f"\n Forza della password: {strength}")
    print(f"🔑 Entropia stimata: {entropy} bit")
    if tips:
        print("\n💡 Suggerimenti:")
        for tip in tips:
            print(f"- {tip}")
