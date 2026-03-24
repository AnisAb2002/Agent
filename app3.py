import streamlit as st
import engine
import mock_agent
import json

# Configuration de la page
st.set_page_config(page_title="VibeGuard IA", page_icon="🛡️", layout="wide")

st.title("🛡️ VibeGuard : Sécurisez votre 'Vibe Coding'")
st.subheader("Évaluez la robustesse de votre agent en un clic.")

# --- INITIALISATION DE L'ÉTAT ---
if 'tests' not in st.session_state:
    st.session_state.tests = None
if 'results' not in st.session_state:
    st.session_state.results = {}

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # 1. LE SÉLECTEUR DE MODE (L'élément critique)
    agent_type = st.radio(
        "Mode de Simulation :", 
        ["Agent Faible (Vibe)", "Agent Robuste (Optimisé)"],
        help="Changez ce mode pour voir comment le Juge réagit à différentes qualités de réponses."
    )
    
    st.divider()
    
    vibe_desc = st.text_area(
        "Description de l'agent :",
        value="Un assistant SAV pour une boutique de sport.",
        height=100
    )
    
    if st.button("🚀 Générer le Banc d'Essai", use_container_width=True):
        with st.spinner("Mistral génère les tests..."):
            response = engine.generate_test_suite(vibe_desc)
            st.session_state.tests = response.get('scenarios', [])
            st.session_state.results = {} # Reset
            st.success("Tests générés !")

# --- ÉTAPE 2 : EXÉCUTION DES TESTS ---
if st.session_state.tests:
    st.header("🧪 Évaluation de l'Agent")
    
    for i, test in enumerate(st.session_state.tests):
        with st.expander(f"Test #{i+1} : {test['nom']}", expanded=True):
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.info(f"**Entrée :** {test['input_utilisateur']}")
                st.write(f"**Attendu :** {test['attendu']}")
            
            with col2:
                # LOGIQUE DE DÉCISION : On récupère la réponse de mock_agent EN DIRECT
                if "Faible" in agent_type:
                    valeur_auto = mock_agent.simuler_reponse_agent_faible(test['input_utilisateur'])
                else:
                    valeur_auto = mock_agent.simuler_reponse_agent_robuste(test['input_utilisateur'])
                
                # IMPORTANT : On force la valeur avec 'value' pour que ça change dès qu'on clique sur la sidebar
                agent_resp = st.text_area(
                    f"Réponse simulée de l'Agent", 
                    value=valeur_auto, 
                    key=f"input_{agent_type}_{i}", # La clé change avec le type d'agent pour forcer le refresh
                    height=100
                )
                
                if st.button(f"Lancer le Juge sur le Test #{i+1}", key=f"btn_{i}"):
                    with st.spinner("Analyse..."):
                        res = engine.evaluate_run(test, agent_resp)
                        st.session_state.results[i] = res
                
                # Affichage du score
                if i in st.session_state.results:
                    res = st.session_state.results[i]
                    if res.get('status') == "SUCCESS":
                        st.success(f"✅ {res['status']} | Note: {res.get('score', 'N/A')}")
                    else:
                        st.error(f"❌ {res['status']} | Note: {res.get('score', 'N/A')}")
                    st.write(f"**Critique du Juge :** {res.get('feedback')}")

# --- ÉTAPE 3 : AMÉLIORATION ---
if st.session_state.results:
    st.divider()
    if st.button("✨ Obtenir des conseils d'amélioration (Basé sur les échecs)"):
        with st.spinner("Analyse Mistral..."):
            tips = engine.get_improvement_tips(vibe_desc, str(st.session_state.results))
            st.success("Analyse terminée !")
            st.write(tips.get('conseils', ["Pas de conseils"]))
            st.code(tips.get('nouveau_prompt_suggere', ""), language="markdown")