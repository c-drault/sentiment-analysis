# Sentiment Analysis Project

## 📦 Install with Docker

### Image from GitHub Package :
- First, you must generate a GitHub token (https://github.com/settings/tokens).
- Once you have your token, let run this : 
```bash
cat ~/TOKEN.txt | docker login https://docker.pkg.github.com -u USERNAME --password-stdin
```
- Pull the image : 
```bash
docker pull docker.pkg.github.com/c-drault/sentiment-analysis/sentiment-analysis:1.0
```
- And then, run a container :
```bash
docker run -p 5000:5000 -d docker.pkg.github.com/c-drault/sentiment-analysis/sentiment-analysis:1.0
```
