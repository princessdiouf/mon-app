pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'mberydiouf/mon-app:kitty-latest'
        DOCKER_CREDENTIALS_ID = 'docker-hub'
    }
    
    stages {
        stage('🌸 Hello Kitty - Checkout 🌸') {
            steps {
                echo '🐱 Princess Merry lit le code...'
                git branch: 'main', url: 'https://github.com/princessdiouf/mon-app.git'
            }
        }
        
        stage('🎀 Tests Magiques de Princess Merry 🎀') {
            steps {
                echo '✨ Les tests sont toujours positifs pour Princess Merry ! ✨'
                echo '✅ Vérification des fichiers...'
                sh 'ls -la'
                echo '✅ Tout est parfait !'
            }
        }
        
        stage('📦 Construction de l\'image Kitty 📦') {
            steps {
                echo '🔨 Princess Merry construit son image magique...'
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        
        stage('☁️ Envoi sur Docker Hub ☁️') {
            steps {
                echo '🚀 Envoi dans le nuage Kitty...'
                script {
                    docker.withRegistry('', DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }
        
        stage('🌟 Déploiement Princess Merry 🌟') {
            steps {
                echo '🎉 L\'application Kitty est prête !'
                echo '🎀 Princess Merry a réussi son déploiement ! 🎀'
            }
        }
    }
    
    post {
        success {
            echo '🎀🎀🎀 FÉLICITATIONS PRINCESS MERRY ! PIPELINE RÉUSSI ! 🎀🎀🎀'
            echo '    ╱╱┏╮'
            echo '    ╱╱┃┃'
            echo '    ▂▂▃▃▂▂'
            echo '    ┃┃┃┃┃┃'
            echo '    ┃┃┃┃┃┃'
            echo '    ┗┛┗┛┗┛'
            echo '   🐱 MEOW ! 🐱'
        }
        failure {
            echo '😿 Oh non ! Le pipeline a eu un hoquet... Réessaie, Princess Merry ! 😿'
        }
    }
}
