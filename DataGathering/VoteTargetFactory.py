
class VoteTargetFactory:

    def classifyVote(v):
        if v== 'SIM':
            return True
        else:
            return False

    def get(df):
        return df['Voto'].map(lambda v: VoteTargetFactory.classifyVote(v))