Se crea el cluster con las siguientes caracteristicas
![image](https://github.com/user-attachments/assets/62431f4d-e9f6-4b07-93a8-6deb1974559e)
![image](https://github.com/user-attachments/assets/ee59f8cf-c7d5-4a1a-bbb3-1d2d22a94b16)
![image](https://github.com/user-attachments/assets/7f701c9c-8dfc-4428-ac1c-b21e7c736b72)
![image](https://github.com/user-attachments/assets/4dffea36-a169-43c4-9622-93d5a523b433)
![image](https://github.com/user-attachments/assets/b18e7acd-1866-465a-8543-f0e6bdf7d620)
![image](https://github.com/user-attachments/assets/41641576-3626-42e0-aacd-29d6bf13724f)

Cuando se haya creado configura los puertos del security group segun los puertos de las aplicaciones de tu cluster:
Puertos de las aplicaciones que necesitas abrir:
- JupyterHub
- Tonalidad (Hue)
- Zeppelin
![image](https://github.com/user-attachments/assets/cc045642-e949-46a8-8acd-cc36dbf08445)

Tambien necesitas habilitar puertos TCP como:
- 14000
- 22
- 9870
![image](https://github.com/user-attachments/assets/01edb33b-ec6c-45ce-886b-2e3c1cb9cc73)

Ve a EC2 y encontraras 3 instancias, 1 sera el nodo master y las otras 2 seran los slaves
![image](https://github.com/user-attachments/assets/c6cb7a69-71de-4d5b-b949-36ab6f13234b)

Verifica que tu bucket este creado y sea el mismo que el de tu cluster
![image](https://github.com/user-attachments/assets/1e30a92a-6bff-4779-beef-f122fac33b2a)

En tus aplicaciones dale click al URL del Hue que en este caso se llamara Tonalidad
![image](https://github.com/user-attachments/assets/cc045642-e949-46a8-8acd-cc36dbf08445)

Alli te pedira que ingreses con usuario y contraseña, asegurate de usar hadoop como usuario y elige una contraseña de tu gusto
![image](https://github.com/user-attachments/assets/47e135e7-8e37-454e-92d3-69f25df56ee2)

Esto veras cuando ingreses
![image](https://github.com/user-attachments/assets/0341201b-dd6c-4677-80d0-45e1783518bc)

Para ingresar a Jupyter haz click en la aplicacion de JupyterHub
![image](https://github.com/user-attachments/assets/cc045642-e949-46a8-8acd-cc36dbf08445)

Alli te pedira que ingreses con usuario y contraseña, asegurate de usar jovyan como usuario y jupyter como contraseña
![image](https://github.com/user-attachments/assets/38478e5d-da21-4cbd-ad89-61d1a6b7ad76)

Esto veras cuando ingreses
![image](https://github.com/user-attachments/assets/07a84fb2-780b-4324-80dd-8405f4104302)
