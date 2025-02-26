describe('Fibonacci App', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('should display the title', () => {
    cy.get('h1').should('contain', 'Fibonacci Sequence Generator');
  });

  it('should have an input field for the number', () => {
    cy.get('input').should('exist');
    cy.get('input').should('have.attr', 'type', 'number');
  });

  it('should have a calculate button', () => {
    cy.get('button').should('exist');
    cy.get('button').should('contain', 'Calculate');
  });

  it('should calculate the Fibonacci sequence for a valid input', () => {
    cy.get('input').type('10');
    cy.get('button').click();
    cy.get('p').should('contain', '0, 1, 1, 2, 3, 5, 8, 13, 21, 34');
  });

  it('should not calculate Fibonacci sequence for a negative number', () => {
    cy.get('input').type('-5');
    cy.get('button').click();
    cy.get('p').should('contain', 'Enter or select a positive integer');
  });

  it('should not calculate Fibonacci sequence for zero', () => {
    cy.get('input').type('0');
    cy.get('button').click();
    cy.get('p').should('contain', 'Enter or select a positive integer');
  });

  it('should not calculate Fibonacci sequence for a non-integer input', () => {
    cy.get('input').type('abc');
    cy.get('button').click();
    cy.get('p').should('contain', 'Enter or select a positive integer');
  });

  it('should clear the sequence when the input is changed', () => {
    cy.get('input').type('10');
    cy.get('button').click();
    cy.get('p').should('contain', '0, 1, 1, 2, 3, 5, 8, 13, 21, 34');
    cy.get('input').clear().type('5');
    cy.get('p').should('contain', 'Enter or select a positive integer');
  });

  it('should calculate the Fibonacci sequence for a large input', () => {
    cy.get('input').type('20');
    cy.get('button').click();
    cy.get('p').should('contain', '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181');
  });

  it('should not allow empty input', () => {
    cy.get('input').clear();
    cy.get('button').click();
    cy.get('p').should('contain', 'Enter or select a positive integer');
  });
});