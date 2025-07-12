"""Component information dataclass for representing manifest files."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Product:
    """Represents a product item in a component manifest.
    
    A product defines an installable item with its identifier and type.
    """
    
    id: str
    type: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Product:
        """Create a Product instance from a dictionary.
        
        Args:
            data: Dictionary containing product data.
            
        Returns:
            Product instance.
        """
        return cls(id=data["id"], type=data["type"])


@dataclass
class ComponentInfo:
    """Represents component information from a manifest file.
    
    This dataclass encapsulates all the metadata about a component including
    its image name, version, type, dependencies, architecture support, and products.
    """
    
    image_name: str
    type: str
    image_version: str
    arch: list[str]
    products: list[Product] | None = None
    depends_on: list[str] | None = None
    heavyweight: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ComponentInfo:
        """Create a ComponentInfo instance from a dictionary.
        
        Args:
            data: Dictionary containing component manifest data.
            
        Returns:
            ComponentInfo instance.
        """
        products = None
        if "products" in data:
            products = [Product.from_dict(product) for product in data["products"]]
        
        return cls(
            image_name=data["image_name"],
            type=data["type"],
            image_version=data["image_version"],
            arch=data["arch"],
            products=products,
            depends_on=data.get("depends_on"),
            heavyweight=data.get("heavyweight"),
        )

    @classmethod
    def from_manifest_file(cls, manifest_path: Path) -> ComponentInfo:
        """Load ComponentInfo from a manifest.json file.
        
        Args:
            manifest_path: Path to the manifest.json file.
            
        Returns:
            ComponentInfo instance loaded from the file.
            
        Raises:
            FileNotFoundError: If the manifest file doesn't exist.
            json.JSONDecodeError: If the manifest file contains invalid JSON.
        """
        with manifest_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)

    def to_dict(self) -> dict[str, Any]:
        """Convert ComponentInfo to a dictionary.
        
        Returns:
            Dictionary representation of the component info.
        """
        result: dict[str, Any] = {
            "image_name": self.image_name,
            "type": self.type,
            "image_version": self.image_version,
            "arch": self.arch,
        }
        
        if self.products is not None:
            result["products"] = [{"id": p.id, "type": p.type} for p in self.products]
        
        if self.depends_on is not None:
            result["depends_on"] = self.depends_on
        
        if self.heavyweight is not None:
            result["heavyweight"] = self.heavyweight
        
        return result

    def to_json(self, indent: int = 2) -> str:
        """Convert ComponentInfo to JSON string.
        
        Args:
            indent: Number of spaces for JSON indentation.
            
        Returns:
            JSON string representation of the component info.
        """
        return json.dumps(self.to_dict(), indent=indent)

    @property
    def full_image_name(self) -> str:
        """Get the full image name with version.
        
        Returns:
            Full image name in format "image_name:image_version".
        """
        return f"{self.image_name}:{self.image_version}"

    @property
    def is_base_component(self) -> bool:
        """Check if this is a base component.
        
        Returns:
            True if the component type is "base", False otherwise.
        """
        return self.type == "base"

    @property
    def is_install_component(self) -> bool:
        """Check if this is an install component.
        
        Returns:
            True if the component type is "install_component", False otherwise.
        """
        return self.type == "install_component"

    @property
    def is_heavyweight(self) -> bool:
        """Check if this is a heavyweight component.
        
        Returns:
            True if heavyweight is set to 1 or greater, False otherwise.
        """
        return self.heavyweight is not None and self.heavyweight >= 1