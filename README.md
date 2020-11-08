# Sentiment Analysis Project ❤️

## Install

This project require Docker 🐳 to be install !

### Image from GitHub Package 📦
First, you must generate a GitHub token (https://github.com/settings/tokens).

Once you have your token, let run this :

```sh
cat ~/TOKEN.txt | docker login https://docker.pkg.github.com -u USERNAME --password-stdin
```

Pull the image : 

```sh
docker pull docker.pkg.github.com/c-drault/sentiment-analysis/sentiment-analysis:1.0
```

And then, run a container :

```bash
docker run -p 5000:5000 -d docker.pkg.github.com/c-drault/sentiment-analysis/sentiment-analysis:1.0
```

### Image from DockerHub 🐳
- First connect to DockerHub
```bash
docker login --username=yourhubusername --email=youremail@company.com
```

Pull the image : 

```sh
docker pull cdrault/sentiment-analysis:1.0
```

And then, run a container :

```bash
docker run -p 5000:5000 -d cdrault/sentiment-analysis:1.0
```
