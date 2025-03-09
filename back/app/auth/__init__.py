"""
Authentication module for handling JWT tokens and verification.

This module provides functionality for JWT token creation, updates,
configuration and verification through the following components:

- JWT_C: Handles token creation, updates and configuration
- auth_service: Provides token verification functionality
"""


from .JWT_C import token_crietor, token_update, jwt_config
from .auth_service import token_verify