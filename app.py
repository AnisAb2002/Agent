import streamlit as st
import engine
import mock_agent
import json

# Configuration de la page
st.set_page_config(page_title="VibeGuard IA", page_icon="🛡️", layout="wide")

st.title("🛡️ VibeGuard : Sécurisez votre 'Vibe Coding'")
st.subheader("Passez du prototype à l'application robuste sans toucher au code.")

# --- INITIALISATION DE L'ÉTAT (Session State) ---
if 'tests' not in st.session_state:
    st.session_state.tests = None
if 'results' not in st.session_state:
    st.session_state.results = {}

# --- BARRE LATÉRALE : CONFIGURATION ---
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Choix du mode pour la démo
    demo_mode = st.toggle("🚀 Mode Démo Automatique", value=True)
    if demo_mode:
        agent_type = st.radio("Simuler quel agent ?", ["Agent Faible (Vibe)", "Agent Robuste (Optimisé)"])
    
    st.divider()
    
    vibe_desc = st.text_area(
        "Décrivez votre agent (votre 'vibe') :",
        value="Un assistant pour une boutique de sport qui gère les prix et les remboursements.",
        placeholder="Ex: Un bot qui aide les étudiants à trouver un stage...",
        height=150
    )
    
    if st.button("🚀 Générer le Banc d'Essai", use_container_width=True):
        with st.spinner("Mistral génère vos scénarios de test..."):
            response = engine.generate_test_suite(vibe_desc)
            st.session_state.tests = response.get('scenarios', [])
            st.session_state.results = {} # Reset des résultats pour les nouveaux tests
            st.success(f"{len(st.session_state.tests)} tests générés !")

# --- ÉTAPE 2 : EXÉCUTION DES TESTS ---
if st.session_state.tests:
    st.header("🧪 Banc d'Essai Automatique")
    
    for i, test in enumerate(st.session_state.tests):
        with st.expander(f"Test #{i+1} : {test['nom']}", expanded=True):
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.info(f"**Contexte :** {test['contexte']}")
                st.write(f"**Entrée utilisateur :** {test['input_utilisateur']}")
                st.write(f"**Attendu :** {test['attendu']}")
            
            with col2:
                # Logique de remplissage automatique pour la démo
                current_val = ""
                if demo_mode:
                    if agent_type == "Agent Faible (Vibe)":
                        current_val = mock_agent.simuler_reponse_agent_faible(test['input_utilisateur'])
                    else:
                        current_val = mock_agent.simuler_reponse_agent_robuste(test['input_utilisateur'])
                
                # Zone de saisie (pré-remplie si mode démo)
                agent_resp = st.text_area(f"Réponse de votre Agent (#{i+1})", value=current_val, key=f"resp_{i}")
                
                if st.button(f"Évaluer Test #{i+1}", key=f"btn_{i}"):
                    with st.spinner("Le Juge analyse..."):
                        res = engine.evaluate_run(test, agent_resp)
                        st.session_state.results[i] = res
                        st.rerun() # Pour mettre à jour l'affichage immédiatement
                
                # Affichage du résultat du Juge
                if i in st.session_state.results:
                    result = st.session_state.results[i]
                    if result.get('status') == "SUCCESS":
                        st.success(f"✅ {result['status']} (Score: {result.get('score', 'N/A')})")
                    else:
                        st.error(f"❌ {result['status']} (Score: {result.get('score', 'N/A')})")
                    st.write(f"**Feedback :** {result.get('feedback', 'Pas de feedback')}")

# --- ÉTAPE 3 : AMÉLIORATION CONTINUE ---
if (st.session_state.tests and len(st.session_state.results) >= len(st.session_state.tests)):
    st.divider()
    st.header("📈 Rapport d'Amélioration")
    
    if st.button("🪄 Générer des conseils d'optimisation"):
        with st.spinner("Analyse des faiblesses en cours..."):
            summary = str(st.session_state.results)
            tips = engine.get_improvement_tips(vibe_desc, summary)
            
            st.write("### 💡 Conseils pour votre prompt :")
            for tip in tips.get('conseils', []):
                st.write(f"- {tip}")
            
            st.markdown("#### ✨ Nouveau Prompt Suggéré :")
            st.code(tips.get('nouveau_prompt_suggere', ""), language="markdown")
            st.balloons()