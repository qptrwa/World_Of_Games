#!/bin/bash
pipeline {
    agent any
    environment {
        registry = "qptrwa/world_of_games"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    stages {
      stage('Build image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Run') {
            steps {
                sh "docker-compose up -d"
            }
        }
        stage('selenium test') {
            steps {
                sh "python tests/e2e.py"
            }
        }
    }
    post {
        always {
            script {
                docker.withRegistry("", registryCredential ) {
                    dockerImage.push()
                }
            }
            sh "docker-compose down"
            sh "docker rmi $registry:$BUILD_NUMBER"
            cleanWs()
        }
    }
}
