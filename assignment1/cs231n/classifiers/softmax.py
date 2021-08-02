from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange
import math
def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train=X.shape[0]
    num_class=W.shape[1]
    for i in range(num_train):
        scores=X[i].dot(W)
        scores=np.exp(scores)
        sum_scores=np.sum(scores)
        soft_scores=scores/sum_scores
        loss-=np.log(soft_scores[y[i]])
        for j in range(num_class):
            if(j==y[i]):
                dW[:,j]+=(soft_scores[j]-1)*X[i].T
            else:
                dW[:,j]+=soft_scores[j]*X[i].T
    loss=loss/num_train+0.5*reg*np.sum(W**2)
    dW=dW/num_train+reg*W
    pass
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    num_train=X.shape[0]
    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    scores=X.dot(W)
    scores=np.exp(scores)
    row_sum=np.sum(scores,axis=1).reshape(num_train,1)
    correct_scores=scores[np.arange(num_train),y]
    #soft_scores=np.divide(scores,row_sum)
    scores/=row_sum
    #scores[np.arange(num_train)]/=row_sum[np.arange(num_train)]
    loss-=np.sum(np.log(scores[np.arange(num_train),y]))
    loss/=num_train
    loss+=0.5*reg*np.sum(W**2)
    scores[np.arange(num_train),y]-=1
    dW=X.T.dot(scores)/num_train+reg*W
    
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
