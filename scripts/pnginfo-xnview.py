from modules import script_callbacks

def add_comment(params:script_callbacks.ImageSaveParams):
    info = params.pnginfo.get('parameters', None)
    texts = [info, "Softwere: Stable Diffusion web UI AUTOMATIC1111"]
    new_info = ", ".join(texts)
    params.pnginfo['Comment'] = new_info

script_callbacks.on_before_image_saved(add_comment)
