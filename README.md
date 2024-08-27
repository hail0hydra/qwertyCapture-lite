# qwertyCapture-demo 👺

<br>
<br>

> #### Disclaimer: ☠  for educational purposes only. User of the application is solely responsible by themselves in case of any malicious activity. ☠

<br>
<br>

- [x]  Simple tool that helps you to simulate and better underrstand how a keylogger works on a Windows based environment.

- [x]  added persistance features

- [x]  Requires Windows OS.  

---

<br>
<br>

## Usage

<br>
<br>

> ⚠️  Better to do this in a VM ⚠️

<br>
<br>

1. make sure no application named __`Windows Explorer.exe`__ is present in location __`%AppData%`__ of your _Windows instance_.

2. make sure the __VIRUS & THREAT PROTECTION__ is turned off for this to work.

3. git clone 🤡 this repo or download it:
    
    ```cmd
    git clone https://github.com/hail0hydra/qwertyCapture-demo.git
    ```

4. Go inside the directory and make a venv 🔽 :

   ```cmd
   $ cd qwertyCapture-demo
   $ python -m venv venv
   $ .\venv\Scripts\activate
   ```
5. Install all requirements
    
    ```cmd
    pip install -r requirements.txt
    ```

6. Ensure `pyinstaller` is sourced in you path:

    ```cmd
    pyinstaller -v
    ```

7. run the `hive.py` file

    ```cmd
    python hive.py
    ```

8. restart your system 🆕

    ```cmd
    shutdown /r /t 0
    ```

9. go to __`%PUBLIC%\Documents`__ and see the logs __key_logs.txt__ 😸 


<br>
<br>

---

<br>
<br>

### Inspiration

```text
In one my classes, we were talking about Keyloggers and hence I made a demo on it :)
```


<br>
<br>
<br>

---

<br>
<br>

### Implementation 📹

- Thank you 🙏 [uzu](https://www.youtube.com/@uzumakiuchiha7678/featured) for the implementation [here](https://www.youtube.com/watch?v=22sA9KCdtsU)
