pipeline {
    parameters {
        string(name: 'ENVIRONMENT', defaultValue: 'dev', description: '')
    }
  agent any
  stages {
    stage('Install sam-cli') {
      steps {
        sh 'python3 -m venv venv && venv/bin/pip install aws-sam-cli'
        stash includes: '**/venv/**/*', name: 'venv'
      }
    }
    stage('Build') {
      steps {
        unstash 'venv'
        sh 'venv/bin/sam build'
        stash includes: '**/.aws-sam/**/*', name: 'aws-sam'
      }
    }
    // stage('beta') {
    //   environment {
    //     STACK_NAME = 'sam-app-beta-stage'
    //     S3_BUCKET = 'cloudfront0307'
    //   }
    //   steps {
    //     withAWS(credentials: 'sam-jenkins-demo-credentials', region: 'us-west-2') {
    //       unstash 'venv'
    //       unstash 'aws-sam'
    //       sh 'venv/bin/sam deploy --stack-name $STACK_NAME -t template.yaml --s3-bucket $S3_BUCKET --capabilities CAPABILITY_IAM'
    //       dir ('hello-world') {
    //         sh 'npm ci'
    //         sh 'npm run integ-test'
    //       }
    //     }
    //   }
    // }
    stage('prod') {
      environment {
        STACK_NAME = 'sam-app-prod-stage'
        S3_BUCKET = 'cloudfront0307'
      }
      steps {
        withAWS(credentials: 'sam-jenkins-demo-credentials', region: 'us-east-2') {
          unstash 'venv'
          unstash 'aws-sam'
          sh 'venv/bin/sam deploy --stack-name $STACK_NAME --no-confirm-changeset --no-fail-on-empty-changeset -t template.yaml --config-file ${ENVIRONMENT}-config.toml --config-env ${ENVIRONMENT} --s3-bucket $S3_BUCKET --capabilities CAPABILITY_IAM'
        }
      }
    }
  }
}