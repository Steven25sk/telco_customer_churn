tensorflow_model_server --port=8500 --rest_api_port="${PORT}" --model_name="${MODEL_NAME}" --model_base_path="${MODEL_BASE_PATH}/${MODEL_NAME}" "$@"


# heroku login
# heroku create churn-backend-v1
# heroku container:login
# heroku container:push web -a churn-backend-v1
# heroku container:release web -a churn-backend-v1