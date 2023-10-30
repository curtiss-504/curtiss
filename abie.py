import random
import pickle

def generer_nombre_cache(interval):
    return random.randint(interval[0], interval[1])

def est_nombre_valide(nombre, interval):
    return interval[0] <= nombre <= interval[1]

def calculer_score(chances_restantes):
    return chances_restantes * 30

def charger_scores():
    try:
        with open('scores.pkl', 'rb') as fichier_scores:
            scores = pickle.load(fichier_scores)
    except (FileNotFoundError, EOFError):
        scores = {}
    return scores

def enregistrer_scores(scores):
    with open('scores.pkl', 'wb') as fichier_scores:
        pickle.dump(scores, fichier_scores)

def johns_jeu_de_roulette():
    print("Bienvenue au johns jeu de roulette!")
    intervalle = [0, 50]
    scores = charger_scores()
    
    while True:
        pseudo = input("Entrez votre pseudo (en minuscules, sans espaces): ")
        if ' ' in pseudo:
            print("Le pseudo ne doit pas contenir d'espaces. Réessayez.")
            continue
        if pseudo.lower() == 'k':
            break
        
        if pseudo in scores:
            ancien_score = scores[pseudo]
        else:
            ancien_score = 0
        
        print(f"Partie en cours pour {pseudo}. Interval: {intervalle}")
        nombre_cache = generer_nombre_cache(intervalle)
        chances_restantes = 10
        
        while chances_restantes > 0:
            try:
                nombre_utilisateur = input(f"Entrez un nombre entre {intervalle[0]} et {intervalle[1]} (ou 'K' pour quitter): ")
                
                if nombre_utilisateur.lower() == 'k':
                    break
                
                nombre_utilisateur = int(nombre_utilisateur)
                
                if not est_nombre_valide(nombre_utilisateur, intervalle):
                    print("Nombre en dehors de l'intervalle. Réessayez.")
                    continue
                
                if nombre_utilisateur == nombre_cache:
                    score = calculer_score(chances_restantes)
                    scores[pseudo] = ancien_score + score
                    enregistrer_scores(scores)
                    print("BRAVO! Vous avez gagné.")
                    print(f"Votre score dans cette partie est: {score}")
                    break
                else:
                    chances_restantes -= 1
                    print(f"Nombre incorrect. Chances restantes: {chances_restantes}")
            
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
        
        else:
            print(f"Désolé, vous avez perdu. Le nombre caché était {nombre_cache}.")
        
        rejouer = input("Voulez-vous rejouer? (Oui/Non): ")
        if rejouer.lower() != 'oui':
            break

    print("Merci d'avoir joué à johns jeu de roulette!")

if __name__ == "__main__":
    johns_jeu_de_roulette()
