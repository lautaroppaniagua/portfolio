import os
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image



with st.container():
    menu = option_menu('Menu',['Español', 'English'], icons=['translate','translate'],
                       orientation='horizontal')



profile_pic = Image.open('source/perfil.png')

header  = Image.open('source/conny-schneider-pREq0ns_p_E-unsplash.jpg')
st.image(header,use_column_width='auto')


column1,column2 = st.columns([0.70,0.2])

with column1:
    st.title('Lautaro Paniagua')
    st.subheader('Data Scientist')
    st.markdown("""
<a href="https://www.linkedin.com/in/lautaroppaniagua/" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-tile.svg" alt="Linkedin" width="30" height="30"/>
    </a>
<a href="https://github.com/lautaroppaniagua" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/github/github-tile.svg" alt="GitHub" width="30" height="30"/>
    </a>
<a href="mailto:lautaroppaniagua@gmail.com" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/gmail/gmail-tile.svg" alt="E-Mail" width="30" height="30"/>
    </a>                
                       
""",unsafe_allow_html=True)
    
with column2:
    st.image(profile_pic, width=100)


if menu=='Español':
    
    st.header('Sobre mí')
    st.markdown(""" 
Soy Lautaro, un estudiante de ingeniería en sistemas con pasión por la ciencia de datos. Siempre estoy en busca de oportunidades para combinar mi experiencia técnica con el mundo del análisis de datos.

Estoy constantemente perfeccionando mis habilidades en el campo de la ciencia de datos. A medida que avanzo en mis estudios, me encuentro cautivado por el inmenso potencial de los datos para revolucionar industrias y resolver desafíos del mundo real.

Estoy entusiasmado por explorar la convergencia entre la ingeniería y la ciencia de datos para crear soluciones innovadoras que tengan un impacto positivo en las empresas y la sociedad. Siempre aprendiendo y adaptándome, prospero en entornos colaborativos que fomentan la creatividad y el pensamiento crítico.
""")
    
    st.header('Lenguajes y herramientas')


    st.markdown(""" 
<div style="border: 2px solid white; padding: 10px; border-radius: 5px;">
  <p align="left">
    <a href="https://hadoop.apache.org/" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-icon.svg" alt="hadoop" width="80" height="80"/>
    </a>
    <a href="https://hive.apache.org/" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/apache_hive/apache_hive-icon.svg" alt="hive" width="80" height="80"/>
    </a>
    <a href="https://www.linux.org/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="80" height="80"/>
    </a>
    <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="80" height="80"/>
    </a>
    <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="80" height="80"/>
    </a>
    <a href="https://www.postgresql.org" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="80" height="80"/>
    </a>
    <a href="https://www.python.org" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="80" height="80"/>
    </a>
    <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer">
      <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="80" height="80"/>
    </a>
    <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer">
      <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="80" height="80"/>
    </a>
    <a href="https://www.selenium.dev" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="80" height="80"/>
    </a>
    <a href="https://pytorch.org" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="PyTorch" width="80" height="80"/>
    </a>
    <a href="https://git-scm.com" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="Git" width="80" height="80"/>
    </a>
    <a href="https://powerbi.microsoft.com/es-es/" target="_blank" rel="noreferrer">
      <img src="https://upload.vectorlogo.zone/logos/microsoft_powerbi/images/985205ac-fb3d-4c80-97f4-7bc0fec8c67d.svg" alt="PowerBI" width="80" height="80"/>
    </a>            
  </p>
</div>
                

""",
unsafe_allow_html=True)
    
    st.header('Proyectos')

    st.markdown("""
## - [Buenos Aires car accidents analysis](https://github.com/lautaroppaniagua/PI_DA)
En este proyecto tome el rol de un analista de datos, utilizando los datasets oficiales de la ciudad de Buenos Aires explore y limpié los datos para realizar graficos y conclusiones sobre los siniestros viales en la ciudad. Por ultimo implemente un dashboard en Tableau que permite al usuario una experiencia mas interactiva para filtrar los graficos y KPIs de los datos a su gusto.
##### Herramientas
Python | Pandas | Matplotlib | Seaborn | Tableau
                
---               
                
## - [Steam recommendation system](https://github.com/lautaroppaniagua/Steam_ML_OPS)
Desarrolle una Rest API en FastAPI y con deploy en Railway en donde se retorna distintas queries sobre un dataset muy extenso proveniente de una base de datos de Steam. A este proyecto tambien le implemente un algoritmo de recomendacion de videojuegos y usuarios para encontrar afinidades entre estos.
##### Herramientas
Python | Pandas | SkLearn | FastAPI
                
---
""", unsafe_allow_html=False)







if menu=='English':
    st.header('About me')
    st.markdown("""I'm Lautaro, a 20 years old aspiring engineer with a passion for data science. I am constantly seeking opportunities to combine my technical expertise with the world of data analytics and insights.

I am actively honing my skills in the field of data science. As I progress in my studies, I find myself captivated by the immense potential of data to revolutionize industries and solve real-world challenges.

I am enthusiastic about exploring the convergence of engineering and data science to create innovative solutions that positively impact businesses and society. Continuously learning and adapting, I thrive in collaborative environments that encourage creativity and critical thinking. """)
    
    st.header('Languages and tools')


    st.markdown(""" 
<div style="border: 2px solid white; padding: 10px; border-radius: 5px;">
  <p align="left">
    <a href="https://hadoop.apache.org/" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-icon.svg" alt="hadoop" width="80" height="80"/>
    </a>
    <a href="https://hive.apache.org/" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/apache_hive/apache_hive-icon.svg" alt="hive" width="80" height="80"/>
    </a>
    <a href="https://www.linux.org/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="80" height="80"/>
    </a>
    <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="80" height="80"/>
    </a>
    <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="80" height="80"/>
    </a>
    <a href="https://www.postgresql.org" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="80" height="80"/>
    </a>
    <a href="https://www.python.org" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="80" height="80"/>
    </a>
    <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer">
      <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="80" height="80"/>
    </a>
    <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer">
      <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="80" height="80"/>
    </a>
    <a href="https://www.selenium.dev" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="80" height="80"/>
    </a>
    <a href="https://pytorch.org" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="PyTorch" width="80" height="80"/>
    </a>
    <a href="https://git-scm.com" target="_blank" rel="noreferrer">
      <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="Git" width="80" height="80"/>
    </a>
    <a href="https://powerbi.microsoft.com/es-es/" target="_blank" rel="noreferrer">
      <img src="https://upload.vectorlogo.zone/logos/microsoft_powerbi/images/985205ac-fb3d-4c80-97f4-7bc0fec8c67d.svg" alt="PowerBI" width="80" height="80"/>
    </a>            
  </p>
</div>
                

""",
unsafe_allow_html=True)
    
    st.header('Projects')

    st.markdown("""
## - [Buenos Aires car accidents analysis](https://github.com/lautaroppaniagua/PI_DA)
In this project, I assumed the role of a data analyst, meticulously delving into the data, conducting thorough cleaning and preprocessing. I harnessed the data to create insightful visualizations and draw meaningful conclusions, all seamlessly presented through an interactive dashboard designed to monitor its dynamic evolution.
##### Tools
Python | Pandas | Matplotlib | Seaborn | Tableau
                
---               
                
## - [Steam recommendation system](https://github.com/lautaroppaniagua/Steam_ML_OPS)
I designed and deployed a REST API hosted on Railway, enabling seamless access to a vast steam dataset. The API seamlessly integrates a powerful recommender system, facilitating data retrieval and recommendations with ease.
##### Tools
Python | Pandas | SkLearn | FastAPI
                
---
""", unsafe_allow_html=False)

