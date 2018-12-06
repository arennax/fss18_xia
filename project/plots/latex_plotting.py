
import os

from plots.parse_outputs import reading

model_names = ['albrecht', 'desharnais', 'finnish', 'kemerer', 'maxwell',
               'miyazaki', 'china', 'isbsg10', 'kitchenham']


def plot_latex_mre(model_index, model_name):
    reading(model_index, model_name)
    cmd = 'cat ' + model_name \
          + '_mre.txt| python2 utils/stats.py --text 30 --latex True | grep \'} \\\\\\\\$\' >> r.txt'
    with open('tmp.sh', 'w') as f:
        f.write(cmd)
    os.system(cmd)

    with open('r.txt', 'r') as myfile:
        data = myfile.read()
    os.system('rm *_*.txt r.txt tmp.sh')
    return data


def plot_latex_sa(model_index, model_name):
    reading(model_index, model_name)
    cmd = 'cat ' + model_name + '_sa.txt| python2 utils/stats.py --text 30 --latex True --higher True | grep \'} \\\\\\\\$\' >> r.txt'
    with open('tmp.sh', 'w') as f:
        f.write(cmd)
    os.system(cmd)

    with open('r.txt', 'r') as myfile:
        data = myfile.read()

    os.system('rm *_*.txt r.txt tmp.sh')
    return data


def plot_mre_for_all():
    """
    PRINTING TO A FILE mre-latex.txt
    :return:
    """
    f = open('Outputs/mre-latex.txt', 'w')
    for i, name in enumerate(model_names):
        print(name)
        P = plot_latex_mre(i, name)
        f.write('\\nm{' + name + '}\\\\' + '\n')
        f.write(P)
    f.close()


def plot_sa_for_all():
    """
        PRINTING TO A FILE sa-latex.txt
        :return:
        """
    f = open('Outputs/sa-latex.txt', 'w')
    for i, name in enumerate(model_names):
        print(name)
        P = plot_latex_sa(i, name)
        f.write('\\nm{' + name + '}\\\\' + '\n')
        f.write(P)
    f.close()


if __name__ == '__main__':
    plot_mre_for_all()
    plot_sa_for_all()
