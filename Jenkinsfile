pipeline {
    agent any
    environment {
        ECR_REGISTRY = "496043249726.dkr.ecr.us-east-1.amazonaws.com"
        APP_REPO     = "order-svc"
        IMAGE_TAG    = "build-${BUILD_NUMBER}"
    }
    stages {
        stage('Fetch Code') {
            steps {
                checkout scm
            }
        }
        stage('AWS ECR Login') {
            steps {
                sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                dir('services/order-svc') {
                    sh "docker build -t ${ECR_REGISTRY}/${APP_REPO}:${IMAGE_TAG} ."
                    sh "docker push ${ECR_REGISTRY}/${APP_REPO}:${IMAGE_TAG}"
                }
            }
        }
        stage('Update K8s Manifests') {
            steps {
                sh """
                    sed -i 's|image: ${ECR_REGISTRY}/${APP_REPO}:.*|image: ${ECR_REGISTRY}/${APP_REPO}:${IMAGE_TAG}|g' k8s-manifests/order-svc.yaml
                    git config user.name "Jenkins CI"
                    git config user.email "jenkins@world.com"
                    git add k8s-manifests/order-svc.yaml
                    git commit -m "chore: automated image tag update to ${IMAGE_TAG} [skip ci]"
                    git push origin main
                """
            }
        }
    }
}
