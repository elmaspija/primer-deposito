import streamlit as st 
from PIL import Image  
import requests 
from streamlit_lottie import st_lottie

st.set_page_config(page_title="valerapp", page_icon="🧊", layout="wide") 

#ae utiliza el with para decir que vas a usar un contenedor
with st.container(): 
    st.header("hola somos valerapp👋") 
    st.title("creamos aplicaciones web con streamlit") 
    st.write("somos unos apasionados de la tecnología y la programación")  
    
    #para agregar un link
    st.write("[saber mas >](https://valerapp.com)")  
    
#le estaba errando porque el url estaba mal, debia ser .json
url= ("https://lottie.host/ed755444-28d4-4624-8f68-40a2a0aa5d56/RSfnmkZCHT.json")

def load_lottie(url): 
     r= requests.get(url)  
    
     #porque 200?  
     #200 es el codigo de respuesta que indica que la solicitud ha tenido éxito,ejm: 404 es que no se encontro la pagina y 500 que vuelvas a intentar
     if r.status_code != 200: 
      return None  
     return r.json()

lottie= load_lottie(url)   

    
with st.container():   
    #linea de separación
    st.write("---")
    text_column, text_animation = st.columns(2) 
    with text_column: 
     st.header("¿Qué hacemos?") 
     st.write(''' 
              Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización. Seguramente te vamos a poder ayudar si:

Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
Quieres mejorar la experiencia de tus clientes
Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo
Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página
              ''')
     
     #duda: porque va con conchete?
     st.write("[mas sobre nosotros>](https://valerapp.com/about)") 
    
    with text_animation: 
     st_lottie(lottie, height=400)



#SERVICIOS 
#diseño de aplicasiones web
with st.container(): 
    st.write("---") 
    st.header("servicios")  
    # DUDA: poque 2 numerales?
    st.write("##") 
    image_colum,text_column=st.columns((1,2))  
    with image_colum: 
        image =Image.open("imagenes/compu.jpg")   

      
        #DUDA: porque use_container_width=True?
        st.image(image,width=200, use_container_width=True) 
        
    with text_column: 
        st.subheader("diseño de aplicasiones web") 
        st.write(''' 
                 si en tus procesos diarios tienes que introducir informacion en diferentes fuentes de datos o bien tienes que trabajar con documentacion
                 ''') 
        st.write("[ver servicios >](https://valerapp.com/services)") 
         
    #AUTOMATIZACIONES 
with st.container(): 
    st.write("---") 
    # DUDA: poque 2 numerales?  
    #agrega un titulo pero como no agregamos nada se ve como una sepacion    
    st.write("##") 
    image_colum,text_column=st.columns((1,2))  
    with image_colum: 
     image =Image.open("imagenes/robot.jpg")  
     
     #el use_column_width=True se utiliza para que la imagen se ajuste a todo el ancho de la columna
     st.image(image,width=200, use_container_width=True )         
     
     
    with text_column: 
        st.subheader("automatizaciones de procesos")  
        st.write(''' 
                 Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras tareas más productivas.
                 ''') 
        st.write("[ver servicios >](https://valerapp.com/services)")      
         
         
#DISEÑO DE BASES DE DATOS  
with st.container(): 
    st.write("---") 
    # DUDA: poque 2 numerales?
    st.write("##") 
    image_colum,text_column=st.columns((1,2))  
    with image_colum: 
     image =Image.open("imagenes/visualizacion d datos.jpg")  
     
     #el use_column_width=True se utiliza para que la imagen se ajuste a todo el ancho de la columna
     st.image(image,width=200, use_container_width=True )         
     
     
    with text_column: 
        st.subheader("visualizacion de datos")  
        st.write(''' 
Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una aplicación en la que puedas tener toda la información de interes de tu empresa.''') 
        st.write("[ver servicios >](https://valerapp.com/services)")      


         
#CONTACTO
st.write("---")
with st.form("my_form"):   
    
    #unsafe_allow_html=True: se utiliza para que se pueda escribir html en el código
    st.write('<input type="hidden" name="_captcha" value="false">', unsafe_allow_html=True)

    st.write("**Formulario de Contacto**")
    name = st.text_input("Nombre")
    email = st.text_input("Correo electrónico")
    phone = st.text_input("Número de teléfono")
    submitted = st.form_submit_button("Enviar")

if submitted:
    st.write("¡Gracias por tu mensaje!")
    st.write(f"Nombre: {name}")
    st.write(f"Correo electrónico: {email}") 
    st.write(f"Número de teléfono: {phone}")