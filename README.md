# Leetcode

# How to clone, push first init commit and create SSH key

git clone https://github.com/shiqi47zzz/Leetcode.git
cd Leetcode
echo "# Leetcode" >> README.md
git init
git add README.md
git commit -m "first commit"
ls -al ~/.ssh
ssh-keygen -t ed25519 -C "https://github.com/shiqi47zzz"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub -> result need to be added on Github where sshkey creation
ssh -T git@github.com
git remote add origin git@github.com:shiqi47zzz/Leetcode.git
git push 