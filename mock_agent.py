def simuler_reponse_agent_faible(input_utilisateur):
    """
    Simule un agent 'Vibe' mal configuré.
    Il est évasif, manque de politesse et ne donne pas d'informations concrètes.
    Objectif : Provoquer un 'FAILURE' lors du test.
    """
    input_lower = input_utilisateur.lower()
    
    # Cas de remboursement
    if "remboursement" in input_lower or "rembourser" in input_lower:
        return "Je ne gère pas ça. Allez voir ailleurs ou cherchez sur le site."
    
    # Cas de prix ou tarifs
    elif "prix" in input_lower or "combien" in input_lower or "tarif" in input_lower:
        return "Les prix changent tout le temps, je ne peux pas vous dire."
    
    # Cas de contact ou aide
    elif "aide" in input_lower or "contact" in input_lower or "humain" in input_lower:
        return "Désolé, je suis juste un bot."
        
    # Réponse par défaut très pauvre
    else:
        return "Euh... je n'ai pas compris votre question. Essayez de demander autre chose."


def simuler_reponse_agent_robuste(input_utilisateur):
    """
    Simule un agent bien configuré après passage par VibeGuard.
    Il est poli, précis et propose des solutions concrètes.
    Objectif : Obtenir un 'SUCCESS' lors du test.
    """
    input_lower = input_utilisateur.lower()
    
    # Cas de remboursement
    if "remboursement" in input_lower or "rembourser" in input_lower:
        return ("Je comprends votre demande. Chez SportShop, vous avez 30 jours pour changer d'avis. "
                "Veuillez me fournir votre numéro de commande pour lancer la procédure de retour.")
    
    # Cas de prix ou tarifs
    elif "prix" in input_lower or "combien" in input_lower or "tarif" in input_lower:
        return ("Nos tarifs dépendent de la gamme choisie : nous avons des raquettes à partir de 29€ "
                "pour les débutants et jusqu'à 150€ pour les compétiteurs. Quel est votre budget ?")
    
    # Cas de contact ou aide
    elif "aide" in input_lower or "contact" in input_lower or "humain" in input_lower:
        return ("Je suis là pour vous aider ! Si vous souhaitez parler à un conseiller, "
                "je peux vous transférer au service client ou vous donner leur numéro : 01 02 03 04 05.")
        
    # Réponse par défaut professionnelle
    else:
        return ("Bonjour ! Je suis l'assistant expert de SportShop. Je peux vous renseigner sur nos produits, "
                "nos tarifs ou notre politique de retour. Que puis-je faire pour vous ?")