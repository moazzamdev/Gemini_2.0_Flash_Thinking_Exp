# import streamlit as st
#
# from langchain_google_genai import ChatGoogleGenerativeAI
#
# import time
# def details():
#     apiKey = "AIzaSyC9ScRqi9g-YghNuS5w7o7Erwtd5RIN_Zo"
#     llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-thinking-exp-01-21", google_api_key=apiKey)
#     st.header("Introducing Gemini")
#     with st.chat_message("assistant"):
#         for chunk in llm.stream("Tell me about google gemini ai model"):
#             st.write(chunk.content)
import time

import streamlit as st

# Ensure set_page_config is at the top
#st.set_page_config(page_title="Gemini 2.0 Flash Thinking", layout="wide")

def details():
    st.empty()
    chat = st.container()
    chat.empty()
    html_code = """
    <!DOCTYPE html>
<html dir="ltr" lang="en">
 <head>
  <meta content="157101835696-ooapojlodmuabs2do2vuhhnf90bccmoi.apps.googleusercontent.com" name="google-signin-client-id"/>
  <meta content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award" name="google-signin-scope"/>
  <meta content="Google AI for Developers" property="og:site_name"/>
  <meta content="website" property="og:type"/>
  <meta content="#1967d2" name="theme-color"/>
  <meta charset="utf-8"/>
  <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <link crossorigin="use-credentials" href="/_pwa/googledevai/manifest.json" rel="manifest"/>
  <link crossorigin="" href="//www.gstatic.com" rel="preconnect"/>
  <link crossorigin="" href="//fonts.gstatic.com" rel="preconnect"/>
  <link crossorigin="" href="//fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="//apis.google.com" rel="preconnect"/>
  <link crossorigin="" href="//www.google-analytics.com" rel="preconnect"/>
  <link href="//fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&amp;display=swap" rel="stylesheet"/>
  <link href="//fonts.googleapis.com/css2?family=Material+Icons&amp;family=Material+Symbols+Outlined&amp;display=block" rel="stylesheet"/>
  <link href="https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai/css/app.css" rel="stylesheet"/>
  <link disabled="" href="https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai/css/dark-theme.css" rel="stylesheet"/>
  <link href="https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai/images/favicon-new.png" rel="shortcut icon"/>
  <link href="https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai/images/touchicon-180-new.png" rel="apple-touch-icon"/>
  <link href="https://ai.google.dev/gemini-api/docs/thinking" rel="canonical"/>
  <link href="https://ai.google.dev/s/opensearch.xml" rel="search" title="Google AI for Developers" type="application/opensearchdescription+xml"/>
  <link href="https://ai.google.dev/gemini-api/docs/thinking" hreflang="en" rel="alternate">
   <link href="https://ai.google.dev/gemini-api/docs/thinking" hreflang="x-default" rel="alternate">
    <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=ar" hreflang="ar" rel="alternate">
     <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=bn" hreflang="bn" rel="alternate">
      <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn" hreflang="zh-Hans" rel="alternate">
       <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw" hreflang="zh-Hant" rel="alternate">
        <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=fa" hreflang="fa" rel="alternate">
         <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=fr" hreflang="fr" rel="alternate">
          <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=de" hreflang="de" rel="alternate">
           <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=he" hreflang="he" rel="alternate">
            <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=hi" hreflang="hi" rel="alternate">
             <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=id" hreflang="id" rel="alternate">
              <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=it" hreflang="it" rel="alternate">
               <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=ja" hreflang="ja" rel="alternate">
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=ko" hreflang="ko" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=pl" hreflang="pl" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br" hreflang="pt-BR" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=ru" hreflang="ru" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=es-419" hreflang="es-419" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=th" hreflang="th" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=tr" hreflang="tr" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=vi" hreflang="vi" rel="alternate"/>
                <link href="https://ai.google.dev/gemini-api/docs/thinking?hl=sq" hreflang="sq" rel="alternate"/>
                <title>
                 Gemini 2.0 Flash Thinking  |  Gemini API  |  Google AI for Developers
                </title>
                <meta content="Gemini 2.0 Flash Thinking  |  Gemini API  |  Google AI for Developers" property="og:title"/>
                <meta content="https://ai.google.dev/gemini-api/docs/thinking" property="og:url"/>
                <meta content="https://ai.google.dev/static/site-assets/images/share-gemini-api.png" property="og:image"/>
                <meta content="1200" property="og:image:width"/>
                <meta content="675" property="og:image:height"/>
                <meta content="en" property="og:locale"/>
                <meta content="summary_large_image" name="twitter:card"/>
                <script type="application/ld+json">
                 {
    "@context": "https://schema.org",
    "@type": "Article",
    
    "headline": "Gemini 2.0 Flash Thinking"
  }
                </script>
                <script type="application/ld+json">
                 {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{
      "@type": "ListItem",
      "position": 1,
      "name": "Gemini API",
      "item": "https://ai.google.dev/gemini-api"
    },{
      "@type": "ListItem",
      "position": 2,
      "name": "Gemini 2.0 Flash Thinking",
      "item": "https://ai.google.dev/gemini-api/docs/thinking"
    }]
  }
                </script>
                <link href="/extras.css" rel="stylesheet"/>
               </link>
              </link>
             </link>
            </link>
           </link>
          </link>
         </link>
        </link>
       </link>
      </link>
     </link>
    </link>
   </link>
  </link>
 </head>
 <body appearance="" class="" display-toc="" layout="docs" pending="" template="page" theme="googledevai-theme" type="article">
  <devsite-progress id="app-progress" type="indeterminate">
  </devsite-progress>
  <a class="skip-link button" href="#main-content">
   Skip to main content
  </a>
  
    
   <section id="gc-wrapper">
    <main class="devsite-main-content" id="main-content" role="main">
     
     <devsite-content>
      <article class="devsite-article">
       
       
       <h1 class="devsite-page-title" tabindex="-1">
        Gemini 2.0 Flash Thinking
        <div class="devsite-actions" data-nosnippet="">
        </div>
       </h1>
       <div class="devsite-page-title-meta">
        <devsite-view-release-notes>
        </devsite-view-release-notes>
       </div>
       <devsite-toc class="devsite-nav" depth="2" devsite-toc-embedded="">
       </devsite-toc>
       <div class="devsite-article-body clearfix">
        <p>
        </p>
        <p>
         The Gemini 2.0 Flash Thinking model is an experimental model that's trained to
generate the "thinking process" the model goes through as part of its response.
As a result, the Flash Thinking model is capable of stronger reasoning
capabilities in its responses than the Gemini 2.0 Flash Experimental model.
        </p>
        <div>
         <a class="button button-primary ais" href="https://aistudio.google.com/prompts/new_chat?model=gemini-2.0-flash-thinking-exp-01-21">
          Try the latest Flash Thinking model in Google AI Studio
         </a>
        </div>
        <h2 data-text="Use thinking models" id="use-thinking-models" tabindex="-1">
         Use thinking models
        </h2>
        <p>
         Flash Thinking models are available in
         <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-2.0-flash-thinking-exp-01-21">
          Google AI Studio
         </a>
         and through the Gemini API. The Gemini API doesn't return thoughts in the response.
        </p>
        <aside class="note">
         <strong>
          Note:
         </strong>
         <span>
          We have set up
          <code dir="ltr" translate="no">
           gemini-2.0-flash-thinking-exp
          </code>
          as an alias to the latest
Flash Thinking model. Use this alias to get the latest Flash thinking model, or
specify the full model name.
         </span>
        </aside>
        <h3 data-text="Send a basic request" id="send-basic" tabindex="-1">
         Send a basic request
        </h3>
        <div class="ds-selector-tabs" data-ds-scope="code-sample">
         <section>
          <h3 data-text="Python" id="python" tabindex="-1">
           Python
          </h3>
          <p>
           This example uses the new
           <a href="/gemini-api/docs/sdks#python-quickstart">
            Google Genai SDK
           </a>
           and the
           <code dir="ltr" translate="no">
            v1alpha
           </code>
           version of the API.
          </p>
          <div>
          </div>
          <devsite-code>
           <pre class="devsite-click-to-copy" dir="ltr" is-upgraded="" syntax="Python" translate="no"><code dir="ltr" translate="no"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">api_key</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'GEMINI_API_KEY'</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">http_options</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s1">'api_version'</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s1">'v1alpha'</span><span class="devsite-syntax-p">})</span>

<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">models</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">generate_content</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'gemini-2.0-flash-thinking-exp'</span><span class="devsite-syntax-p">,</span>
    <span class="devsite-syntax-n">contents</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'Explain how RLHF works in simple terms.'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>

<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre>
          </devsite-code>
         </section>
        </div>
        <h3 data-text="Multi-turn thinking conversations" id="multi-turn-thinking" tabindex="-1">
         Multi-turn thinking conversations
        </h3>
        <p>
         During multi-turn conversations, thoughts from previous turns are stripped from
the model's inputs.
        </p>
        <div class="ds-selector-tabs" data-ds-scope="code-sample">
         <section>
          <h3 data-text="Python" id="python_1" tabindex="-1">
           Python
          </h3>
          <p>
           The new
           <a href="/gemini-api/docs/sdks#python-quickstart">
            Google Genai SDK
           </a>
           provides the ability to create a multi-turn chat session which is
helpful to manage the state of a conversation.
          </p>
          <div>
          </div>
          <devsite-code>
           <pre class="devsite-click-to-copy" dir="ltr" is-upgraded="" syntax="Python" translate="no"><code dir="ltr" translate="no"><span class="devsite-syntax-kn">from</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-nn">google</span><span class="devsite-syntax-w"> </span><span class="devsite-syntax-kn">import</span> <span class="devsite-syntax-n">genai</span>

<span class="devsite-syntax-n">client</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">genai</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">Client</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">api_key</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'GEMINI_API_KEY'</span><span class="devsite-syntax-p">,</span> <span class="devsite-syntax-n">http_options</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-p">{</span><span class="devsite-syntax-s1">'api_version'</span><span class="devsite-syntax-p">:</span><span class="devsite-syntax-s1">'v1alpha'</span><span class="devsite-syntax-p">})</span>

<span class="devsite-syntax-n">chat</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-n">client</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">aio</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">chats</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">create</span><span class="devsite-syntax-p">(</span>
    <span class="devsite-syntax-n">model</span><span class="devsite-syntax-o">=</span><span class="devsite-syntax-s1">'gemini-2.0-flash-thinking-exp'</span><span class="devsite-syntax-p">,</span>
<span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">chat</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_message</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'What is your name?'</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-n">response</span> <span class="devsite-syntax-o">=</span> <span class="devsite-syntax-k">await</span> <span class="devsite-syntax-n">chat</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">send_message</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-s1">'What did you just say before this?'</span><span class="devsite-syntax-p">)</span>
<span class="devsite-syntax-nb">print</span><span class="devsite-syntax-p">(</span><span class="devsite-syntax-n">response</span><span class="devsite-syntax-o">.</span><span class="devsite-syntax-n">text</span><span class="devsite-syntax-p">)</span>
</code></pre>
          </devsite-code>
         </section>
        </div>
        <h2 data-text="Limitations" id="limitations" tabindex="-1">
         Limitations
        </h2>
        <p>
         The Flash Thinking model is an experimental model and has the following
limitations:
        </p>
        <ul>
         <li>
          No JSON mode or Search Grounding
         </li>
         <li>
          Thoughts are only shown in Google AI Studio
         </li>
        </ul>
        <h2 data-text="What's next?" id="whats-next" tabindex="-1">
         What's next?
        </h2>
        <ul>
         <li>
          Try the Flash Thinking model in
          <a href="https://aistudio.google.com/prompts/new_chat?model=gemini-2.0-flash-thinking-exp-01-21">
           Google AI Studio
          </a>
          .
         </li>
         <li>
          Try the
          <a href="https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking.ipynb">
           Flash Thinking Colab
          </a>
          .
         </li>
        </ul>
        <link data-page-link="" href="/site-assets/css/style.css?v=3" rel="stylesheet"/>
        <link data-page-link="" href="https://fonts.googleapis.com/css2?family=Google+Symbols:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
       </div>
      </article>
    </main>
    
  <script nonce="JcFvBGdkcv/1Vce7ZjN/RLoNxR4Uj2">
   (function(d,e,v,s,i,t,E){d['GoogleDevelopersObject']=i;
    t=e.createElement(v);t.async=1;t.src=s;E=e.getElementsByTagName(v)[0];
    E.parentNode.insertBefore(t,E);})(window, document, 'script',
    'https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai/js/app_loader.js', '[59,"en",null,"/js/devsite_app_module.js","https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933","https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai","https://googledevai-dot-devsite-v2-prod-3p.appspot.com",null,null,["/_pwa/googledevai/manifest.json","https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/images/video-placeholder.svg","https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai/images/favicon-new.png","https://www.gstatic.com/devrel-devsite/prod/v17c4f87be230ffee20589ee6dca0a2318ead9eddb228ec5c58233202ff69a933/googledevai/images/lockup-new.svg","https://fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&display=swap"],1,null,[1,6,8,12,14,17,21,25,50,52,63,70,75,76,80,87,91,92,93,97,98,100,101,102,103,104,105,107,108,109,110,112,113,116,117,118,120,122,124,125,126,127,129,130,131,132,133,134,135,136,138,140,141,147,148,149,151,152,156,157,158,159,161,163,164,168,169,170,179,180,182,183,186,191,193,196],"AIzaSyCNm9YxQumEXwGJgTDjxoxXK6m1F-9720Q","AIzaSyCc76DZePGtoyUjqKrLdsMGk_ry7sljLbY","ai.google.dev","AIzaSyB9bqgQ2t11WJsOX8qNsCQ6U-w91mmqF-I","AIzaSyAdYnStPdzjcJJtQ0mvIaeaMKj7_t6J_Fg",null,null,null,["Search__enable_ai_eligibility_checks","Concierge__enable_actions_menu","DevPro__enable_developer_subscriptions","MiscFeatureFlags__enable_project_variables","Cloud__enable_llm_concierge_chat","MiscFeatureFlags__developers_footer_dark_image","MiscFeatureFlags__emergency_css","MiscFeatureFlags__developers_footer_image","MiscFeatureFlags__enable_framebox_badge_methods","Profiles__enable_page_saving","MiscFeatureFlags__enable_explain_this_code","Cloud__enable_cloud_shell_fte_user_flow","DevPro__enable_cloud_innovators_plus","Cloud__enable_cloud_shell","Concierge__enable_pushui","MiscFeatureFlags__enable_view_transitions","BookNav__enable_tenant_cache_key","CloudShell__cloud_shell_button","Cloud__enable_cloud_dlp_service","TpcFeatures__enable_unmirrored_page_left_nav","Profiles__enable_completecodelab_endpoint","Profiles__enable_profile_collections","Profiles__enable_recognition_badges","OnSwitch__enable","Profiles__enable_completequiz_endpoint","Cloud__enable_free_trial_server_call","Search__enable_page_map","Profiles__enable_stripe_subscription_management","DevPro__enable_devpro_offers","Cloud__enable_legacy_calculator_redirect","MiscFeatureFlags__enable_firebase_utm","Experiments__reqs_query_experiments","Analytics__enable_clearcut_logging","Cloud__enable_cloud_facet_chat","Profiles__enable_release_notes_notifications","MiscFeatureFlags__enable_variable_operator_index_yaml","Search__enable_suggestions_from_borg","Profiles__enable_join_program_group_endpoint","Profiles__enable_awarding_url","Profiles__enable_public_developer_profiles","Profiles__enable_developer_profiles_callout","Cloud__enable_cloudx_ping","TpcFeatures__enable_mirror_tenant_redirects","MiscFeatureFlags__enable_variable_operator","Profiles__require_profile_eligibility_for_signin","Profiles__enable_complete_playlist_endpoint","CloudShell__cloud_code_overflow_menu","Profiles__enable_dashboard_curated_recommendations","Cloud__enable_cloudx_experiment_ids","Search__enable_dynamic_content_confidential_banner","EngEduTelemetry__enable_engedu_telemetry"],null,null,"AIzaSyA58TaKli1DculwmAmbpzLVGuWc8eCQgQc","https://developerscontentserving-pa.googleapis.com","AIzaSyDWBU60w0P9hEkr29kkksYs8Z7gvZ8u_wc","https://developerscontentsearch-pa.googleapis.com",2,4,null,"https://developerprofiles-pa.googleapis.com",[59,"googledevai","Google AI for Developers","ai.google.dev",null,"googledevai-dot-devsite-v2-prod-3p.appspot.com",null,null,[null,1,null,null,null,null,null,null,null,null,null,[1],null,null,null,null,null,null,[1],null,null,null,null,[1],[1,1,null,1,1]],null,[73,null,null,null,null,null,"/images/lockup-new.svg","/images/touchicon-180-new.png",null,null,null,1,1,1,null,null,null,null,null,null,null,2,null,null,null,"/images/lockup-dark-theme-new.svg",[]],[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[44,2,4,6,7,12,14,15,17,18,20,21,22,23,28,29,32,37,39,40,43],null,[[],[1,1],null,1],[[null,null,null,null,null,["GTM-TC2MQKS8"],null,null,null,null,null,[["GTM-TC2MQKS8",1]],1]],null,4],null,null,1,1,"https://developerscontentinsights-pa.googleapis.com","AIzaSyBUwhBSZ2D08LlB5muaB5af2QQjzrjYbIw"]')
  </script>
  <devsite-a11y-announce>
  </devsite-a11y-announce>
 </body>
</html>

    """
    data = f'''**Gemini 2.0 Flash Thinking** \n\nThe Gemini 2.0 Flash Thinking model is an experimental model that's trained to generate the "thinking process" the model goes through as part of its response. As a result, the Flash Thinking model is capable of stronger reasoning capabilities in its responses than the Gemini 2.0 Flash Experimental model.\n\n**Use thinking models**\n\nFlash Thinking models are available in Google AI Studio and through the Gemini API. The Gemini API doesn't return thoughts in the response.\n\nNote: The set up for gemini-2.0-flash-thinking-exp as an alias to the latest Flash Thinking model. Use this alias to get the latest Flash thinking model, or specify the full model name. \n\n**Send a basic request**\n\nThis example uses the new Google Genai SDK and the v1alpha version of the API.\n ```python\n from google import genai\nclient = genai.Client(api_key='GEMINI_API_KEY', http_options='api_version':'v1alpha')\nresponse = client.models.generate_content(\nmodel='gemini-2.0-flash-thinking-exp',\ncontents='Explain how RLHF works in simple terms.',\n)\nprint(response.text)\n```\n**Multi-turn thinking conversations**\n\nDuring multi-turn conversations, thoughts from previous turns are stripped from the model's inputs.\nThe new Google Genai SDK provides the ability to create a multi-turn chat session which is helpful to manage the state of a conversation.\n```python\nfrom google import genai\nclient = genai.Client(api_key='GEMINI_API_KEY', http_options='api_version':'v1alpha')\nchat = client.aio.chats.create(\nmodel='gemini-2.0-flash-thinking-exp',\n)\nresponse = await chat.send_message('What is your name?')\nprint(response.text)\nresponse = await chat.send_message('What did you just say before this?')\nprint(response.text)\n```\n\n**Limitations**\n\nThe Flash Thinking model is an experimental model and has the following limitations:\n\n\tNo JSON mode or Search Grounding\n\tThoughts are only shown in Google AI Studio'''

    def stream_data():
        for word in data.split(" "):
            yield word + " "
            time.sleep(0.02)


    time.sleep(3)
    with st.chat_message("assistant", avatar="🤖"):
        st.write_stream(stream_data)
    # Use st.components.v1.html to render full HTML layout properly
    #st.components.v1.html(html_code, height=800, scrolling=True)
    #st.chat_message("user", avatar="🧑").markdown(f'''**Gemini 2.0 Flash Thinking** \n\nThe Gemini 2.0 Flash Thinking model is an experimental model that's trained to generate the "thinking process" the model goes through as part of its response. As a result, the Flash Thinking model is capable of stronger reasoning capabilities in its responses than the Gemini 2.0 Flash Experimental model.\n\n**Use thinking models**\n\nFlash Thinking models are available in Google AI Studio and through the Gemini API. The Gemini API doesn't return thoughts in the response.\n\nNote: The set up for gemini-2.0-flash-thinking-exp as an alias to the latest Flash Thinking model. Use this alias to get the latest Flash thinking model, or specify the full model name. \n\n**Send a basic request**\n\nThis example uses the new Google Genai SDK and the v1alpha version of the API.\n ```python\n from google import genai\nclient = genai.Client(api_key='GEMINI_API_KEY', http_options='api_version':'v1alpha')\nresponse = client.models.generate_content(\nmodel='gemini-2.0-flash-thinking-exp',\ncontents='Explain how RLHF works in simple terms.',\n)\nprint(response.text)\n```\n**Multi-turn thinking conversations**\n\nDuring multi-turn conversations, thoughts from previous turns are stripped from the model's inputs.\nThe new Google Genai SDK provides the ability to create a multi-turn chat session which is helpful to manage the state of a conversation.\n```python\nfrom google import genai\nclient = genai.Client(api_key='GEMINI_API_KEY', http_options='api_version':'v1alpha')\nchat = client.aio.chats.create(\nmodel='gemini-2.0-flash-thinking-exp',\n)\nresponse = await chat.send_message('What is your name?')\nprint(response.text)\nresponse = await chat.send_message('What did you just say before this?')\nprint(response.text)\n```\n\n**Limitations**\n\nThe Flash Thinking model is an experimental model and has the following limitations:\n\n\tNo JSON mode or Search Grounding\n\tThoughts are only shown in Google AI Studio''')

