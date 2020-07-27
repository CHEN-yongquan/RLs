import sys
sys.path.append('../..')

from rls.utils.expl_expt import ExplorationExploitationClass


def test_exploration_exploitation_class():
    my_expl = ExplorationExploitationClass(eps_init=1, eps_mid=0.2, eps_final=0.01, eps_eval=0,
                                           init2mid_annealing_step=50, start_step=0, max_step=100)
    assert my_expl.get_esp(0) == 1
    assert my_expl.get_esp(0, evaluation=True) == 0
    assert my_expl.get_esp(80, evaluation=True) == 0
    assert my_expl.get_esp(2) < 1
    assert my_expl.get_esp(50) == 0.2
    assert my_expl.get_esp(51) < 0.2
    assert my_expl.get_esp(100) >= 0.01

    my_expl = ExplorationExploitationClass(eps_init=0.2, eps_mid=0.1, eps_final=0, eps_eval=0,
                                           init2mid_annealing_step=1000, start_step=0, max_step=10000)
    assert my_expl.get_esp(0) == 0.2
    assert my_expl.get_esp(0, evaluation=True) == 0
    assert my_expl.get_esp(500, evaluation=True) == 0
    assert my_expl.get_esp(500) < 0.2
    assert my_expl.get_esp(1000) == 0.1
    assert my_expl.get_esp(2000) < 0.1
    assert my_expl.get_esp(9000) > 0
