
class VoteTargetFactory:

    def classifyVote(v):
        if v== 'SIM':
            return 'Yes'
        else:
            return 'No'

    def get(df):
        return df['Voto'].map(lambda v: VoteTargetFactory.classifyVote(v))