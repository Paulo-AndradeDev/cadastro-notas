# cadastro-notas

## Como rodar em localhost:

1. Instale o Python 3.7 ou superior. Se assegure de instalar tb o PIP em sua máquina

   > https://www.python.org/downloads/

2. Faça o download ou clone do projeto aqui no github

3. utilize o terminal cmd no windows ou o terminal de alguma IDE, preferencialmente o PyCharm community 

   > https://www.jetbrains.com/pycharm/download/

4. Preferencialmente, crie um ambiente virtual no diretório raiz (um nível acima dos arquivos do projeto)
   
   Ex.: 
      > python -m venv myenv
      
      > myenv\Scripts\activate

5. Com ou sem o ambiente virtual ativado, instale o Django com o seguinte comando: 

   > python -m pip install Django
   

5. Com ou sem o ambiente virtual ativado, vá até a pasta em que se encontra o arquivo requirements.txt e rode o seguinte comando:
  
  >  pip install -U -r requirements.txt
  
  * Isto irá instalar todos os pacotes
  
  
6. vá até a pasta em que se encontra o arquivo manage.py e rode o seguinte comando:

   > python manage.py runserver
   
   
7. Acesse o endereço http://127.0.0.1:8000/admin em seu browser

8. Utilize login 'admin' e senha tb 'admin'


 

