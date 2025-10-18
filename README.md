# Poultry-Diseases-Detection-System

Hello Guys,  
This project implements an end-to-end deep learning pipeline for classifying chicken fecal images to detect potential diseases. Built with TensorFlow and Keras, the system leverages a modular MLOps architecture inspired by industry best practices, ensuring reproducibility, scalability, and maintainability.
In this Project I am addressing 3 Diseases:  
1.Coccidiosis  
2.New Castle Disease  
3.Salmonella  
or else: Healthy Obiviously...

#### 🔧 Key Features:
- **Data Ingestion**: Automated download and extraction of image datasets.
- **Model Preparation**: Loads and customizes a pre-trained CNN (Here, used ResNet50) with transfer learning.
- **Training Pipeline**: Uses `ImageDataGenerator` with augmentation, checkpointing, and TensorBoard logging.
- **Evaluation Module**: Loads the trained model, evaluates on validation data, and logs accuracy/loss metrics.
- **Configuration Management**: All paths and hyperparameters are centralized in `config.yaml` and `params.yaml`.
- **Environment Isolation**: Fully reproducible via Conda environment and version-controlled artifacts.
- **Extensible Design**: Modular class-based structure allows easy integration with DVC, CI/CD, or cloud deployment.

#### 📁 Tech Stack:
- Python, TensorFlow/Keras
- YAML for configuration
- Conda for environment management
- Jupyter/VS Code for development
- (Optional) DVC for data and model versioning

---

