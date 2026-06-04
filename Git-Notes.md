Instead of copying files, rename your existing project folder and connect it directly:

cd "C:\Users\dushyant\Desktop\AI-PROJECT-SELF"

git init
git remote add origin https://github.com/vichara-dushyant/multi-agent-engine.git
git pull origin main --allow-unrelated-histories
git add .
git commit -m "Initial multi-agent framework"
git push -u origin main (-u means "--set-upstream".)