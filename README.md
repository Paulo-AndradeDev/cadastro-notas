# cadastro-notas

[![Watch the video](https://img.youtube.com/vi/x1gyLl1QdM4/0.jpg)](https://youtu.be/x1gyLl1QdM4)

## Como rodar em localhost:

1. Instale o Python 3.7 ou superior. 

   > https://www.python.org/downloads/

2. Faça o download ou clone do projeto aqui no github

3. utilize o terminal cmd no windows ou o terminal de alguma IDE.

4. Ative o ambiente virtual "myenv" no diretório raiz (um nível acima dos arquivos do projeto)
         
      > myenv\Scripts\activate
      
5. Instale os pacote com o comendo:

      > pip install -r requirements.txt

5. No terminal, vá até a pasta em que se encontra o arquivo manage.py (mesmo direitório do arquivo requirements.txt supracitado) e rode o seguinte comando:

      > python manage.py runserver
   
   
7. Acesse o endereço http://127.0.0.1:8000/admin em seu browser

8. Utilize login 'admin' e senha tb 'admin'


 ## Pacotes utilizados:
 
 Django CKEditor
   > https://django-ckeditor.readthedocs.io/en/latest/
 
 Jazzmin
   >https://django-jazzmin.readthedocs.io/
  
  
# Sobre o Robô

o diretório "dist" contém o arquivo executável de um robô que roda a aplicação em um servidor local. 

Esse robô executa a aplicação depois de instalada. Ou seja, na primeira execução é preciso seguir os passo acima até o item 5, pois somente depois de instalados os requerimentos o robô funcionará. 

O código do robô está no arquivo cadnotas.py.
 
Entretanto, o robô está configurado com os arquivos do projeto em C:/cad-notas. Se o seu caminho for difenrente, altere a linha 10 do arquivo cadnotas.py e crie outro executável. 

Para criar um executável:
   > pip install pyinstaller
   
   > pyinstaller --onfile --noconsole cadnotas.py
   
   
 

