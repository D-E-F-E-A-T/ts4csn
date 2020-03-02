from tree_sitter import Language, Parser

Language.build_library(
  # Store the library in the `build` directory
  'build/csn.so',

  # Include one or more languages
  [
    'vendor/tree-sitter-go',
    'vendor/tree-sitter-java',
    'vendor/tree-sitter-javascript',
    'vendor/tree-sitter-php',
    'vendor/tree-sitter-python',
    'vendor/tree-sitter-ruby',
  ]
)

