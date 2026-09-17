from whitenoise.storage import CompressedManifestStaticFilesStorage


class LooseManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """Eksik kaynak dosyalarına (örn. .map dosyaları) toleranslı WhiteNoise storage."""

    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            return name