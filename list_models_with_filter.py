from huggingface_hub import HfApi 

api = HfApi()

models = api.list_models(
    task="text-classification",
    sort="downloads",
    direction=-1,
    limit=5
)
modelList = list(models)
print(modelList[0])