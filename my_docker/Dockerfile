FROM yanwk/comfyui-boot:cu129-slim

RUN pip install "triton<3.3" sageattention requests

COPY download_models.py /opt/download_models.py
RUN chmod +x /opt/download_models.py

EXPOSE 8188

ENV CLI_ARGS="--fast --use-sage-attention --listen 0.0.0.0"

VOLUME ["/root"]