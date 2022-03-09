node {

    stage("Checkout repo"){
        git branch: 'main',
        url: 'https://github.com/YevhenGolishko/python-api-training.git'
    }
    stage("Install deps"){
        sh 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
    }

}
