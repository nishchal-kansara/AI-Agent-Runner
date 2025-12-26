# This function provides recommended training settings
# It is used to explain how training stability and safety can be improved
# These values are suggestions not automatic training steps
def recommended_hyperparameters():
    return {
        # Number of full passes over the dataset
        # Kept low to avoid overfitting on small or low quality data
        "epochs": 3,

        # Controls how fast the model learns
        # A small value helps keep training stable
        "learning_rate": 2e-5,

        # Number of samples processed together
        # Small batches reduce noisy updates
        "batch_size": 4,

        # Limits how large gradient updates can be
        # Helps prevent unstable training behavior
        "gradient_clipping": 1.0,

        # Gradually increases learning rate at the start
        # Helps the optimizer settle smoothly
        "warmup_steps": 50
    }