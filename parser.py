'''
Glossary

Stmt_list       ->      Stmt Stmt_list | ε
Stmt            ->      id = Expr | print Expr
Expr            ->      Term Term_tail
Term_tail       ->      Logic Term Term_tail | ε
Term            ->      Factor Factor_tail
Factor_tail     ->      Parenthesis Factor Factor_tail | ε
Factor          ->      (Expr) | id | true | false | t | f | 1 | 0
Logic           ->      not | and | or
Parenthesis     ->      ( | )
'''

import plex


# ... συμπληρώστε τον κώδικά σας για τον συντακτικό αναλυτή - αναγνωριστή της γλώσσας ...

