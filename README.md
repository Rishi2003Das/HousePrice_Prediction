# HousePrice_Prediction
An end-to-end machine learning model on California House Price dataset from Kaggle, for house price prediction with regression model.

## For creating new environment
Yes! Creating a virtual environment is a great way to manage dependencies and avoid conflicts between package versions. Here’s how you can do it:

### **Step 1: Create a Virtual Environment**
Run the following command in your terminal or command prompt:

```sh
python -m venv myenv
```
Replace `myenv` with any name you prefer for your virtual environment.

### **Step 2: Activate the Virtual Environment**
- **On Windows (cmd or PowerShell):**
  ```sh
  myenv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```sh
  source myenv/bin/activate
  ```

Once activated, your terminal prompt should change, indicating that you work in the virtual environment.

### **Step 3: Install Packages Inside the Virtual Environment**
If you have already installed packages globally and want to install them in your virtual environment, use:

```sh
pip freeze > requirements.txt  # Save installed packages to a file
pip install -r requirements.txt  # Install them in the virtual environment
```

Alternatively, install specific packages using:

```sh
pip install package_name
```

### **Step 4: Verify Installed Packages**
Check installed packages within the virtual environment using:

```sh
pip list
```

### **Step 5: Deactivate the Virtual Environment**
When you're done, deactivate it by running:

```sh
deactivate
```

Would you like help troubleshooting or managing dependencies in your virtual environment? 😊

## To commit the changes in the saved files from the VSCode to github repo

It looks like you're facing an authentication issue while pushing your code to GitHub. The error message suggests that Git is unable to authenticate you properly.

---

### **Possible Causes & Fixes:**
#### **1️⃣ Check Your GitHub Authentication Method**
Since GitHub no longer supports password authentication for Git operations, you should use either **SSH keys** or a **personal access token (PAT)**.

##### **Solution: Use a Personal Access Token (PAT)**
1. Go to **[GitHub Developer Settings](https://github.com/settings/tokens)**.
2. Click **"Generate new token (classic)"**.
3. Select scopes:
   - Check `repo` (for repository access).
4. Click **"Generate token"**.
5. Copy the generated token (you won't see it again).

##### **Use the Token Instead of Your Password**
Now, use the token when pushing:

```sh
git remote set-url origin https://<YOUR_GITHUB_USERNAME>:<YOUR_ACCESS_TOKEN>@github.com/Rishi2003Das/HousePrice_Prediction.git
```

Then, try pushing again:

```sh
git push origin main
```

---

#### **2️⃣ Check Your VS Code Git Authentication**
Since the error mentions VS Code, try restarting VS Code and signing in again:
1. Open VS Code.
2. Press **Ctrl + Shift + P** and search for **"Sign in with GitHub"**.
3. Re-authenticate your GitHub account.

---

#### **3️⃣ Use SSH Instead of HTTPS (Recommended for Long-Term Use)**
If you prefer SSH authentication:
1. Generate an SSH key:
   ```sh
   ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
   ```
2. Add the key to GitHub:
   - Copy the public key:  
     ```sh
     cat ~/.ssh/id_rsa.pub
     ```
   - Go to **GitHub > Settings > SSH and GPG Keys > New SSH Key**.
   - Paste the key and save it.
3. Change the Git remote URL to SSH:
   ```sh
   git remote set-url origin git@github.com:Rishi2003Das/HousePrice_Prediction.git
   ```
4. Try pushing again:
   ```sh
   git push origin main
   ```

---

### **Final Steps**
Try **Solution 1 (PAT)** first. If you work with GitHub frequently, **Solution 3 (SSH)** is the best approach.

Let me know if you need more help! 🚀
